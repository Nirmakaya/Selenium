from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')

## Selenium syntax to upload when there is a 'type' element available
## Type='file' attribute must be there on Uploadfile, for this to work, you can ask DevTeam to add this
#type="file"
driver.find_element(By.NAME, 'upfile').send_keys('C:/Users/ZS174XZ/Downloads/ey-logo-4.png')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(3)