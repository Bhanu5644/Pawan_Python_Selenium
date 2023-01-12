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
#Date of Birth Element
driver.find_element(By.XPATH,"//*[@id='dob']").click()

datepicker_month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
datepicker_month.select_by_visible_text("Dec") # Month Selected
datepicker_year=Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[2]"))
datepicker_year.select_by_visible_text("1991")
alldates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in alldates:
    if date.text=="25":
        date.click()
        break