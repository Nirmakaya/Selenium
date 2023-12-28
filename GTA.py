from selenium import webdriver
from selenium.common import MoveTargetOutOfBoundsException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://qa-eygta.ey.com/auth/login')
driver.implicitly_wait(5)
driver.maximize_window()

act_chains = ActionChains(driver)

time.sleep(5)
User = driver.find_element(By.XPATH, "//label[text()='User']")

Username = driver.find_element(By.XPATH,"//input[@type='text']")


try:
        act_chains.move_to_element(Username).perform()

except MoveTargetOutOfBoundsException as e:
    print(e)
    driver.execute_script("arguments[0].scrollIntoView(true);", Username)

time.sleep(3)




driver.find_element(By.XPATH,"//input[@type='text']").send_keys("gta_user_1@gta.com")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("password@1")
driver.find_element(By.XPATH,"//button[text()=' Login ']").click()
driver.find_element(By.XPATH,"//button[text()='Ok']").click()
time.sleep(2)