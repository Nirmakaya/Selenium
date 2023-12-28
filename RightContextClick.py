from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

'''right/Context Click'''
## This format of comment  will be saved in files of program
web_element = driver.find_element(By.XPATH, '//span[text()="right click me"]')
act_chains = ActionChains(driver)

act_chains.context_click(web_element).perform()

context_list = driver.find_elements(By.CSS_SELECTOR, 'li.context-menu-icon span')

for ele in context_list:
    print(ele.text)
    if ele.text == 'Copy':
        ele.click()
        time.sleep(3)
        break

## ActionChains can also be use to perform send_keys_to_element(without perform()), click() etc

