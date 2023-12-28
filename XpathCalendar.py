import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://ui.cogmento.com//")

## How to handle dynamic calenders:-
## Some months will have different date on the same rows and column
## In Feb if it's a leap year it'll have extra 29th day

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys('suryansh8888@gmail.com')
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys('Suryansh@123')
driver.find_element(By.CSS_SELECTOR, '.ui.fluid.large.blue.submit.button').click()
slider = driver.find_element(By.CSS_SELECTOR, "#main-nav")
action_chains = ActionChains(driver)
action_chains.move_to_element(slider).perform()
time.sleep(3)
driver.find_element(By.XPATH, "//span[contains(text(),'Calendar')]").click()
driver.find_element(By.XPATH, "//div[@class='rbc-date-cell rbc-off-range']//button[normalize-space()='28']").click()
