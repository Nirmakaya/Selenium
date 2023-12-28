from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)


driver.get("https:/www.reddit.com/")
## Normal Screenshot
# driver.get_screenshot_as_file("reddit.png")
# ## Screenshot will be saved at the same file folder

'''full screenshot'''
## To take full screenshot we need to make sure thst it is running in headless mode

## We have used lambda with variable X, and An Java script is used -- {the return type + Varable(X)}
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
## Setting the size of the window, S is behaving like a function
driver.set_window_size(S('Width'), S('Height'))
## Body tag name is used to take screenshot of the entire body or page
driver.find_element(By.TAG_NAME,'body').screenshot('reddit_full_1.png')

