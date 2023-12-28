import xlrd
## XL reader, this will help read Excel sheet with the help of python
## Install xlrd

## Data Driven Approach in selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get('https://www.orangehrm.com/en/30-day-free-trial/')

## To maximise the browser
driver.maximize_window()

url = driver.find_element(By.ID, 'Form_getForm_subdomain')
name = driver.find_element(By.ID, 'Form_getForm_Name')
email = driver.find_element(By.ID, 'Form_getForm_Email')
number = driver.find_element(By.ID, 'Form_getForm_Contact')
country = driver.find_element(By.ID, 'Form_getForm_Country')


excel = xlrd.open_workbook("ExcelForPython.xlsx")

## 1st
sheet = excel.sheet_by_name("login")

# Get Number of rows and column
rowCount = sheet.nrows
colCount = sheet.ncols
print(rowCount)
print(colCount)

# In excel write numeric with single colon like '9999 (otherwise it will take as string/error)
# Print those Rows and column
for curr_row in range(1, rowCount):
    # Row is in curr_row(1) and column = 0 for first column of first row
    username = sheet.cell_value(curr_row, 0)
    # Row is in curr_row and column = 1 for second column of first row
    passCode = sheet.cell_value(curr_row, 1)

    print(username + " " + str(passCode))


## 2nd
## Filling form using excel
sheet = excel.sheet_by_name("registration")

rowCount = sheet.nrows
colCount = sheet.ncols
print(rowCount)
print(colCount)

for curr_row in range(1, rowCount):
    urlValue = sheet.cell_value(curr_row, 0)
    nameValue = sheet.cell_value(curr_row, 1)
    emailValue = sheet.cell_value(curr_row, 2)
    numberValue = sheet.cell_value(curr_row, 3)
    countryValue = sheet.cell_value(curr_row, 4)

    ## Data Filling
    ## .clear() to clear before next entry
    url.clear()
    url.send_keys(urlValue)
    name.clear()
    name.send_keys(nameValue)
    email.clear()
    email.send_keys(emailValue)
    number.clear()
    number.send_keys(numberValue)
    country.send_keys(countryValue)
    time.sleep(3)



