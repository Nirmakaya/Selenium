## Search boxes which can change it's elements with time
## Like in Google Search bar

# In ul tag, Class may be changed. So select it properties.

## Parent and Child Relationship:-
# This will select all list or child of parent ul tag.
# //ul[@role='idhuer']//

## Decendant:-
# //ul[@role='idhuer']//li/descendant::div[@class='spqf_c']
#
# Descendant is used to go to li tag's div> class. Or to go inside li descendants
## You can use for loop to iterate through list and select the desired value



import time
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://www.google.com/")

search_bar = driver.find_element(By.XPATH, '//textarea[@id="APjFqb"]').send_keys('shraddha sarda')
## Dynamic Custom Xpath
list = driver.find_elements(By.XPATH, "//ul[@role='listbox']//li/descendant::div[@class='wM6W7d']")

print(len(list))

for ele in list:
    print(ele.text)
    if ele.text == 'shraddha sarda':
        ele.click()
        break

time.sleep(5)






