from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select
import time
serv_obj = Service("C:/Users/BHANU/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))
#Approach 1
# for i in range(len(checkboxes)):
    # checkboxes[i].click()
#Approach 2
# for checkbox in checkboxes:
#     checkbox.click()
# Multiple checkboxes select.
# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute('id')
#     if weekname =='monday' or weekname=='friday':
#         checkbox.click()
# if you want to select bottom 2
# for i in range(len(checkboxes)-3,len(checkboxes)):
#     checkboxes[i].click()
#Approach Select First 2:
for i in range(len(checkboxes)):
    if i < 3:
        checkboxes[i].click()
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.clear()
