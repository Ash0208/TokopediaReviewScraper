from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import random

# Use the review page of a certain product, not the review page for the store itself.
url = "https://www.tokopedia.com/xiaomi/official-poco-x6-pro-5g-dimensity-8300-ultra-120hz-fiow-amoled-67w-t-grey-12-512g-ed3b0/review"

# Ensure the driver starts on a maximised window
options =webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(5)

#Define list to fill with extracted data
data =[]

# i in range("Page amount")
for i in range(50):
    #To show full reviews
    try:
        selengkapnya_buttons = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.css-89c2tx"))
        )
        
        for btn in selengkapnya_buttons:
            try:
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(random.uniform(0.5, 1.5))  # Small delay for content update
            except Exception as e:
                continue

    except Exception as e:
        print(f"No 'Selengkapnya' buttons found or timed out: {e}")

    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    containers = soup.findAll('article', attrs={'class': 'css-72zbc4'})

    for container in containers:
        try:    #Extract reviews and its contents
            review = container.find('span', attrs = {'data-testid':'lblItemUlasan'}).text
        except AttributeError:
            continue
        
        try:    #Extract ratings
            star_element = container.find('div', attrs={'data-testid': 'icnStarRating'})
            star_rating = star_element.get('aria-label', 'bintang 0').split()[-1]  # Extract number
        except AttributeError:
            star_rating = "0"

        data.append((review, star_rating))    #Inputs extracted data to list

    time.sleep(2)
    try:    #Click to next page of reviews
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']"))
        )
        next_button.click()
        time.sleep(3)  # Allow next page to load
    except Exception as e:
        print(f"Failed to click next page: {e}")
        break  # Stop if no next page

 
# Format data into csv
df = pd.DataFrame(data, columns=["Ulasan","Ratings"])
df.to_csv("Scraped Data.csv", index=False)
