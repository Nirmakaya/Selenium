from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


## To run it in headless mode
options = webdriver.ChromeOptions()
## New headless option from 2023 version
# Previous version : options.headless = False
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
## For incognito mode, you can also write to block the popup, or any proxy setting you want to write
# options.add_argument("--incognito")

# ## For firefox
# options = webdriver.FirefoxOptions()
# options.headless = True
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

driver.get("https://amazon.in")
print(driver.title)