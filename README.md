# Tokopedia Review Scraper

## Overview
This script is a web scraper designed to extract product reviews and ratings from Tokopedia using Selenium and BeautifulSoup. The extracted data is saved as a CSV file for further analysis.

## Features
- **Automated Review Extraction**: Scrapes customer reviews and their corresponding star ratings from a specified Tokopedia product page.
- **Pagination Handling**: Automatically navigates through multiple pages to collect a larger dataset.
- **Click Interaction**: Expands full-length reviews by clicking on "Selengkapnya" buttons where applicable.
- **Randomized Delays**: Introduces small random delays between interactions to mimic human behavior and reduce the chance of detection.
- **Data Export**: Saves the extracted data in CSV format for easy analysis.

## Dependencies
- Python 3.x
- Selenium
- BeautifulSoup (bs4)
- Pandas
- Chrome WebDriver

## Installation & Usage
1. **Install Dependencies:**
   ```bash
   pip install selenium beautifulsoup4 pandas
   ```
2. **Ensure Chrome WebDriver is Installed:**
   - Download the appropriate version from [Chrome WebDriver](https://sites.google.com/chromium.org/driver/)
   - Ensure the WebDriver is placed in a directory that is accessible by the script.

3. **Run the Script:**
   ```bash
   python scraper.py
   ```
   - Modify the `url` variable in the script to the desired Tokopedia product review page.

4. **Output:**
   - The extracted reviews and ratings will be saved in `Scraped Data.csv`.

## Disclaimer
This script is intended for educational and research purposes only. Scraping Tokopedia may violate their Terms of Service, so use it responsibly.


