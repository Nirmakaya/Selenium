from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome()

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

wait = WebDriverWait(driver, 10)

driver.find_element(By.NAME, 'proceed').click()

## Waiting for alert to appear, it wil check if there is alert or not
alert = wait.until(expected_conditions.alert_is_present())
print(alert.text)

alert.accept()

driver.close()