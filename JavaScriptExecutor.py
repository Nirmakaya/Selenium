## You can write java script methods on Devtools Console and perform


# For keys
# write document.getElementById('username').value='Username'
#Or use
#
#
# Refresh
# write history.go(0)
#
# Title
# write document.title


## JavaScript Execution using Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


driver.get("https://www.amazon.in/")

bestseller = driver.find_element(By.LINK_TEXT, 'Best Sellers')

## JS code, ends with ;
driver.execute_script("arguments[0].click();", bestseller)

# For title
title = driver.execute_script("return document.title;")
print(title)

## For refresh
driver.execute_script("history.go(0);")

# ## For alert, but this hinders the on going js script
# driver.execute_script("alert('Hii Automation')")
# time.sleep(3)

## This would generate all the inner scripts of the page without the html code, only the actual code
## This can be used for Content Testing
inner_text = driver.execute_script("return document.documentElement.innerText;")
print(inner_text)

## For border change, this can be used before taking screenshot of an error
driver.execute_script("arguments[0].style.border = '3px solid red'", bestseller)
time.sleep(3)

## Scrolling:-

# Scroll to the bottom using JS
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# For Bottom to top
# write driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

## Scroll Down to a particular only till a particular element
BackTotop = driver.find_element(By.XPATH, '//*[@id="CardInstancerch41Wc0lPdLqbEKjt8muQ"]/div[1]/h2')
driver.execute_script("arguments[0].scrollIntoView(true);", BackTotop)
time.sleep(3)
