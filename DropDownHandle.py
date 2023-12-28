from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.orangehrm.com/en/30-day-free-trial/")



ele_country = driver.find_element(By.ID, 'Form_getForm_Country')

select = Select(ele_country)
## Here we select value by text
select.select_by_visible_text('India')
time.sleep(4)


## A generic method created for DropDown insertion
def select_values(selector, value):
    select = Select(selector)
    select.select_by_visible_text(value)
# You may use the above select_value(ele_country, 'India')


# Dropdown Options List
# options keyword is used to select the OPTION TAG or every value from select variable which has the CSS Selector
country_list = select.options

for ele in country_list:
    print(ele.text)
    if(ele.text == 'Australia'):
        ele.click()
        time.sleep(3)
        break



## Selecting DropDown without using Select Class
country_option = driver.find_elements(By.XPATH, '//*[@id="Form_getForm_Country"]/option')
print(len(country_option))
for ele in country_option:
    print(ele.text)
    if ele.text == 'Algeria':
        ele.click()
        time.sleep(3)
        break



## Function of Xpath Dropdown
## This dropdown will work on any kind of dropdown and not only select type dropdown, by using xpath method

def select_values_from_dropdown(DropdownOptionList, value):
    print(len(DropdownOptionList))
    for ele in DropdownOptionList:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break







