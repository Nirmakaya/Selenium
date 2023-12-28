from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()

## Locators can be of BY.LINK_TEXT , ID, XPATH, NAME, CLASS_NAME

## For By.ID use '#' eg. #Username

## By.NAME 'name text'

## With CSS_SELECTOR, class name in place of spaces you have to use dot

## PARTIAL_LINK_TEXT with this, the entire text of link need not be mentioned

## BY.TAG_NAME 'h1', HTML tags are used, dot and hash is not used


driver.find_element(By.CSS_SELECTOR, '')

