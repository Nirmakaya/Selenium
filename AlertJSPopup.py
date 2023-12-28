from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")


## You cannot inspect a popup which is not an web element from DevTools of Chrome
## The popup isn't a web element it has no CSS,XPATH etc
## It is coming because of JavaScript Alert Method, and the whole page freezes
## You can use Console alert('msg') to bring any popup

driver.find_element(By.NAME, 'proceed').click()
time.sleep(3)

## driver moves on to the alert popup
alert = driver.switch_to.alert
print(alert.text)
alert.accept()      #This accepts the popup
# alert.dismiss()     #This declines the popup
# alert.send_keys()     #To pass a comment

## driver back to original page
driver.switch_to.default_content()

time.sleep(3)
driver.quit()