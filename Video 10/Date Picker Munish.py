from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select
import time

serv_obj = Service("C:/Users/BHANU/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
year="2023"
month="March"
date="18"
driver.find_element(By.XPATH,"//*[@id='datepicker']").click() # open date picker element
while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]").click()
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in dates:
    if ele.text==date:
        ele.click()
        break