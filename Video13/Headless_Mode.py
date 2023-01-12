from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def healess_Chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:/Users/BHANU/Downloads/chromedriver_win32/chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver=webdriver.Chrome(service=serv_obj,options=ops)
    return driver
driver = healess_Chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
