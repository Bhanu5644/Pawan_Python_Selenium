from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select
import time
serv_obj=Service("C:/Users/BHANU/Downloads/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#Capture cookies from brwoser
# cookies=driver.get_cookies()
# print("size if cookies:",len(cookies))#3

#print all type of cookies:
# for c in cookies:
#     #print(c)
#     #print(c.get('name'))
#     print(c.get('name'),":",c.get('value'))
# driver.quit()

# Add new cookie in Browser
driver.add_cookie({'name':"My Cookies",'value':"12345"})
cookies=driver.get_cookies()
print("size if cookies after adding new one:",len(cookies))#4

#Delete a specific cookie from Browser
driver.delete_cookie("My Cookies")
cookies=driver.get_cookies()
print("size if cookies after deleteing Specific cookie:",len(cookies))
driver.quit()

# Delete all cookies:
driver.delete_all_cookies()
cookies=driver.get_cookies()
print("size if cookies after deleteing all cookie:",len(cookies))

driver.quit()