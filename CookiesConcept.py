from selenium import webdriver


## Cookies are certain website data of the page that is stored to have access your personal data
## Like what kind of language you use want kind domain you have, or what kind of localisation you have


driver = webdriver.Chrome()

## In DevTools > Network you can find Cookies of that website that are used

driver.get("https://www.reddit.com/")

## To add cookies, we need to give Key value Pair
driver.add_cookie({"name":"naveenpython","domain":"reddit.com","value":"python"})

## This will give dictionaries of cookies
cookies = driver.get_cookies()


for cook in cookies:
    print(cook)

## Or use print(driver.get_cookies())