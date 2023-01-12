from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select
import time

serv_obj = Service("C:/Users/BHANU/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
act = ActionChains(driver)
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(3)
#Admin --> User management--> User
admin = driver.find_element(By.XPATH,"//label[@id='label-tab-open-insurance']").click()
act.move_to_element(admin).move_to_element(Usermanagement).move_to_element(Users).click()

