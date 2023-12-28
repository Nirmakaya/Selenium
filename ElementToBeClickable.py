from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


driver.get("https://app.hubspot.com/login/")

## URL match wait
wait.until(ec.url_contains('hubspot'))

##This will also give the element link
signup_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Sign up')))
print(signup_link.text)
signup_link.click()


## Visiblity of a element : it check if the element is visible on DOM and on the PAge with some width and Height, length

## Waiting for firstname to appear
header_link = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'LandingPageTitle__LandingPageSubtitle-rshrji-1.jxIPii')))


