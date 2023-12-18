from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

url = "https://github.com/scamsniffer/scam-database/blob/main/blacklist/domains.json"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

# go to the releases
driver.find_element(By.XPATH, "//a[@href='/scamsniffer/scam-database/blob/main/blacklist/domains.json?raw=true']").click()
time.sleep(5)
text = driver.find_element(By.XPATH, '//pre[@style="word-wrap: break-word; white-space: pre-wrap;"]').text
time.sleep(3)
text = text.replace("\"", "")
text = text.replace("\n", "")
lst = text.split(',')

# converting the list of url sto a csv file
df = pd.DataFrame(lst)
df.to_csv('blacklist.csv', index=False)

# to drop any duplicates added while updating the list
bl = pd.read_csv('blacklist.csv')
result = bl.drop_duplicates(keep=False)
result.to_csv('blacklist.csv', index=False)

print("Done")