from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://www.spicejet.com/")

'''move to Element '''

SpiceClub = driver.find_element(By.XPATH, '//*[@id="main-container"]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div[1]')
## Action change on chrome page is used
action_chains = ActionChains(driver)
## move_to_element function is used, along with perform function at the end
action_chains.move_to_element(SpiceClub).perform()
time.sleep(3)

Tier_link = driver.find_element(By.LINK_TEXT, 'Tiers')      #Used dot in place of space in class name
time.sleep(3)

Tier_link.click()
time.sleep(3)

driver.quit()
