from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

query="Laptop"

driver.get(f'https://www.amazon.com/s?k={query}&ref=nav_bb_sb')
elem = driver.find_element(By.CLASS_NAME, 'puis-card-container')
print(elem.get_attribute("outerHTML"))

time.sleep(4)

driver.quit()   