from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

query="Laptop"
for i in range(1,20):
    driver.get(f'https://www.amazon.com/s?k={query}&page={i}&ref=nav_bb_sb')
    elems = driver.find_elements(By.CLASS_NAME, 'puis-card-container')
    print(f"{len(elems)} items found " )

    for elem in elems:
        print(elem.text)
# print(elem.get_attribute("outerHTML"))


    time.sleep(2)

driver.quit()       