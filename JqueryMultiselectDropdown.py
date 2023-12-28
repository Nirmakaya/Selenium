from selenium import webdriver
from selenium.webdriver.common.by import By
import time


## Selenium is about creating Generic Utilities Function and distribute them to your team for use
## So in this case we have created a generic function for single, multiple and all Dropdown selection of a page
## These generic functions are important for selenium expertise

# def select_values(drop_list, value):
#     for ele in drop_link:
#         print(ele.text)
#         if ele.text == value:
#             ele.click()
#             break


driver = webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.find_element(By.ID, 'justAnInputBox').click()
time.sleep(2)

drop_link = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
time.sleep(3)

# for ele in drop_link:
#     print(ele.text)
#     if ele.text == 'choice 6 2 3':
#         ele.click()
#         break


# By a generic function we can select multiple values by calling the function,
# In the link multiple values can be selected at once like 2, 3 , 4.2 at a time
# select_values(drop_link, 'choice 2 1')
# select_values(drop_link, 'choice 6 2 3')


## The above selection can become TDS, So we would create another function

option_list = [ 'choice 2 1', 'choice 6 2 3', 'choice 7']

def select_values_byList(drop_link, value):
    if not value[0] == 'all':
        for ele in drop_link:
            print(ele.text)
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    break
    else:
        ##Exception Handling due to ElementNotInteractableException error
        try:
            for ele in drop_link:
                ele.click()
        except Exception as e:          ## e is the exception generated sentence
            print(e)
        ## So Intead of throwing exception it will print the Exception sentence or 'e'


#select_values_byList(drop_link, option_list))


## To select all the values by generic function
all_list = ['all']

select_values_byList(drop_link, all_list)