from selenium import webdriver
from selenium.webdriver.common.by import By

## Static Wait : time.sleep(3), this stops the script for 3 seconds

## Dynamic Wait : wait till the given element isn't visible
## It has two types implicit wait OR webdriver wait/Explicityly wait


driver = webdriver.Chrome()


driver.implicity_wait(10)
## Wait will be applicable for all the web element, Like whenever you do find_element and find_elements
## Only for web element it woeks, Not for title,alert,URL. For that use explicitly wait
## It is also called Global Wait

driver.get("https://app.hubspot.com/login")

## Implicit Wait of 10sec will be applied BYDEFAULT to all the elements of webdriver
user_name = driver.find_element(By.ID, 'username')
user_name.send_keys('test@gmail.com')

driver.find_element(By.ID, 'username').send_keys('test@123')

## BUt this every time wait is unecessary
## Hence,In POM or Data Driven Model we use Explicitly wait

# This overrides the previous implicit wait
driver.implicity_wait(5)
# This nullifies the implicit wait function
driver.implicity_wait(0)

## By default there is a Interval/Poling mechanism by which selenium checks element after every 500ms

## Implicitly wait cannot be apllied for URL,
## Like title of the page, it may give the first loading page title
## For that you use webdriver wait

