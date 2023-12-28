from selenium import webdriver
import time


driver = webdriver.Chrome()

## While using a ID Administration or a Modem Website,
## They ask for logon and passcode before entering the website

## You can put login ID and Passcode before domain name with
## For Login:admin and Passcode:admin @ Eg. admin:admin@
## Username:Password@, but sometimes it doesn't work on firefox,or other websites
time.sleep(3)
driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')