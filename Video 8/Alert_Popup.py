from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select
import time
serv_obj = Service("C:/Users/BHANU/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button').click()
myalert = driver.switch_to.alert
print(myalert.text)
myalert.send_keys("Welcome")
myalert.accept()
#myalert.dismiss() #closing window
