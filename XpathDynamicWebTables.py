## When dynamic data is available in the table under table tag
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://ui.cogmento.com//")

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys('suryansh8888@gmail.com')
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys('Suryansh@123')
driver.find_element(By.CSS_SELECTOR, '.ui.fluid.large.blue.submit.button').click()
driver.find_element(By.CSS_SELECTOR, '.users.icon').click()
driver.find_element(By.CSS_SELECTOR, 'body').click()
time.sleep(3)

## Method 1 : Through Loops, less performance

#
# #In HTML tr = rows, td = column
# # Table xpath of names : //div[@class='table-wrapper']//tbody/tr[1 or 2 or 3 or 4 or ...]/td[2]
# before_xpath = "//div[@class='table-wrapper']//tbody/tr["
# after_xpath = "]/td[2]/a"
#
# for i in range(1,5):
#     name = driver.find_element(By.XPATH, before_xpath+str(i)+after_xpath).text
#     print(name)
#     if name=="Suryansh Prasad":
#         driver.find_element(By.XPATH, "//div[@class='table-wrapper']//tbody/tr["+str(i)+"]/td[1]").click()
#         time.sleep(5)

## Method 2 : By using custom XPATH, it is more fast

driver.find_element(By.XPATH, "//a[text()='TEST demo']//parent::td//preceding-sibling::td[@class]").click()
driver.find_element(By.XPATH, "//a[text()='Ruyx itsu']//parent::td//preceding-sibling::td[@class]").click()
time.sleep(5)




