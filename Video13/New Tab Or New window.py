from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select
import time

serv_obj = Service("C:/Users/BHANU/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# Regislink = Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(Regislink)

#Open new Tab and Switch Window
driver.get('https://www.google.com')
driver.switch_to.new_window("window")
driver.get('https://www.facebook.com')