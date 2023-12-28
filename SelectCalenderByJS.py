from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")

## Selenium can't change the HTML DOM so we have used JS to do that, and change date from it
## This is only applicable where value is there in the calender
## Through java script we are changing value by backend
## so it can change to anything like 40-10-23 is also possible, so we need to be careful with it

def selectDateByJS(date_col, date):

    driver.execute_script("arguments[0].setAttribute('value' , '"+date+"');", date_col)

## Website Doesn't contains 'value' :-(


date_col = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
date = "30 Aug' 23"

selectDateByJS(date_col, date)

