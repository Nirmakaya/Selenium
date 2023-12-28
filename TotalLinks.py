from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# driver.implicitly_wait(10)
#
# driver.get("https://www.freshworks.com/")
# linksList = driver.find_elements(By.TAG_NAME, 'a')
# print(len(linksList))


driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")
linksList = driver.find_elements(By.TAG_NAME, 'a')
print(len(linksList))

## Print using for loop
for ele in linksList:
    print(ele.text)
    print(ele.get_attribute('href'))
    ## This will print every href links with it's respective name



