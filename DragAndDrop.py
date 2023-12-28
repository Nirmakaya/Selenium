from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")

source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')

act_chains = ActionChains(driver)        #This will return a reference which will be stored in act_chains

# Directly Drag and Drop
act_chains.drag_and_drop(source, target).perform()
time.sleep(3)

# Drag and Drop in Steps
act_chains.click_and_hold(source).move_to_element(target).perform()
time.sleep(3)