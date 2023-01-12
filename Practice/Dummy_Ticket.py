from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select
import time


serv_obj = Service("C:/Users/BHANU/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
# driver.find_element(By.XPATH,"//*[@id='select2-reasondummy-container']/span").click()
driver.find_element(By.XPATH,"//input[@class='select2-search__field']").click()

# alloptions = drp.options
# print(" Total no. of options",len(alloptions))

#print all theoptions

# for opt in alloptions:
#     print(opt.text)