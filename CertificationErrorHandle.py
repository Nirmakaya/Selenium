## Certification Concept in https
#
# Server is the host server of the website that we would access
# https protocol sends request to server for secure ssl certification,
# Websites communicates with the Server in encrypted manner in https
# Browser gets certain secure Certificates from the server regarding the website that you would access
# Browser checks if the received certificate is valid or not, and only if it is valid website is accessible
# Else, it will give privacy error that we would learn to bypass in the below code to access the website
# This is only for https http doesn't have this feature

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


## To Bypass, before Launcing the chrome we need to import options()

options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')

## Or use options.set_capability('acceptInsecureCerts', True) and use chrome_options=options in driver Chrome

# Second Method
# capabilities = DesiredCapabilities().CHROME.copy()
# capabilities['acceptInsecureCerts'] = True

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

driver.get("https://expired.badssl.com/")
time.sleep(3)
print(driver.find_element(By.TAG_NAME, 'h1').text)