# Scam Domain Blacklist Scraper

This Python script utilizes Selenium WebDriver to scrape a blacklist of scam domains from a specific GitHub repository and exports the list to a CSV file. It's a straightforward tool for anyone needing to keep an up-to-date list of known scam domains for cybersecurity analysis, research, or web filtering purposes.

## Prerequisites

To run this script, you will need:

- Python 3.x
- Selenium WebDriver
- ChromeDriver (compatible with your Chrome version)
- pandas library

Ensure you have Chrome installed on your system as the script uses ChromeDriver to automate browser interactions.

## Installation

1. **Python 3.x**: If you haven't installed Python 3, download and install it from [python.org](https://www.python.org/downloads/).

2. **Selenium WebDriver**: Install Selenium using pip:

    ```bash
    pip install selenium
    ```

3. **ChromeDriver**: Download ChromeDriver from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads) matching your Chrome version. Extract the executable and place it in a known directory or add it to your PATH.

4. **pandas library**: Install pandas using pip:

    ```bash
    pip install pandas
    ```

## Usage

Before running the script, make sure ChromeDriver is installed and its path is correctly set. Then, you can run the script with:

```bash
python script_name.py
