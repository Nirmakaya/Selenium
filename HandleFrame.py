from selenium import webdriver
from selenium.webdriver.common.by import By

## Frames are things that are not used in modern websites
## Under browser > Under Webpage > Frame > elements,
## So the access frame you need to jump driver on frame first just like for popups

driver = webdriver.Chrome()

driver.get('http://www.londonfreelance.org/courses/frames/index.html')

## For switching to a frame
#driver.switch_to.frame(2)

## switch_to_element can have ID or NAME
driver.switch_to.frame('main')

# frame_element = driver.find_element(By.NAME, 'main')
# driver.switch_to.frame(frame_element)

headerValue = driver.find_element(By.CSS_SELECTOR, 'body > h2').text
print(headerValue)

# First we would switch to parent frame
driver.switch_to.parent_frame()
driver.switch_to.default_content()
