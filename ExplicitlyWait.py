from selenium import webdriver
from selenium.webdriver.common.by import By

## For explicit wait import
from selenium.webdriver.support.wait import WebDriverWait
## Named expected_conditions to ec using 'as' keyword
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get("https://app.hubspot.com/login/")

## Dynamically waiting of 10sec only for driver
wait = WebDriverWait(driver, 10)

## Tile Wait
wait.until(ec.title_is('HubSpot Login'))
print(driver.title)
## For long title you can write -- wait.until.(ec.title_contains('HubSpot')

## Explicitly wait
## presence_of_element_located() takes only one locator so use brackets to manage By
## presence_of_element_located() is waiting for a locator/element to appear inside the 'Dom' of Devtools
## or The DocumnetObjectModel of the HTML source, sometimes element may not be visible on page even if it visible on the dom,
email_id = wait.until(ec.presence_of_element_located((By.ID, 'username')))
email_id.send_keys('test@gmail.com')
## For password we don't need to apply explicitly wait, we can use it directly as it loads with the username
