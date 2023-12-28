from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

## Cross Browsers
browserName = "chrome"

## Instead of writing the executable file everytime, we can import chrome driver manager for chrome,
## But first we need to install the webdriver_manager package
## Then we would automate the installation part in this code

if browserName == "chrome":
    driver = webdriver.Chrome()
elif browserName == "safari":
    driver = webdriver.Safari()
else:
    print("please pass a browser name : " + browserName)
    raise Exception('driver is not there')

driver.implicitly_wait(5)

driver.get("https://app.hubspot.com/login")
driver.find_element(By.ID, 'username').send_keys("hii@gmail.com")
driver.find_element(By.ID, 'password').send_keys("ki")
driver.find_element(By.ID, 'loginBtn').click()

print(driver.title)
time.sleep(3)
driver.quit()





