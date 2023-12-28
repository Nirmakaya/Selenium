from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://amazon.in")
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()
time.sleep(2)
## You cannot inspect the back button of browser
## It isn't part of HTML docs it's a browser property
## For that use below syntax

driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.back()

## For refresh
driver.refresh()

driver.quit()