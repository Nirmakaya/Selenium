## Since selenium is not coming from python package directly, we would import
from selenium import webdriver
## BY package
from selenium.webdriver.common.by import By
import time

# You can use any name instead of driver, like dr
driver = webdriver.Chrome()
##driver = webdriver.Chrome(executable_path="C:\\Users\\ZS174XZ\\OneDrive - EY\\Documents\\Driver\\chromedriver.exe")
## The executable file is already installed by terminal

driver.implicitly_wait(5)
driver.get("https://www.google.com")
print(driver.title)

## Bylocator
driver.find_element(By.NAME, 'q').send_keys('naveen automationlabs')
time.sleep(2)
optionsList = driver.find_elements(By.XPATH, "//ul[@role='listbox']//li/descendant::div[@class='lnnVSe']")

print(len(optionsList))

for ele in optionsList:
    print(ele.text)
    if ele.text == 'naveen automationlabs youtube':
        ele.click()
        break

time.sleep(3)
driver.quit()

##Some problem with CSS SELECTOR

## To run from terminal change directory and type {pytest name.py} OR {python name.py}