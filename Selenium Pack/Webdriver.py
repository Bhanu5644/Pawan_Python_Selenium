from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select
import time

serv_obj=Service("C:/Users/BHANU/Downloads/chromedriver_win32/chromedriver.exe")
# serv_obj=Service("")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)
# driver.find_element(By.NAME,"username").send_keys("Admin")
# driver.find_element(By.CSS_SELECTOR,'input[name="username"]').send_keys("Admin")
driver.find_element(By.XPATH,"//*[@placeholder='Username']").send_keys("Admin")
# driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
Original_Title = driver.title
Expected_Title = 'OrangeHRM'
if Original_Title == Expected_Title:
    print("Test case pass")
else:
    print("Test case not match")
time.sleep(10)
driver.close()
