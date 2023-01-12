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
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
act = ActionChains(driver)
min_slider=driver.find_element(By.XPATH,"//span[1]")
max_slider=driver.find_element(By.XPATH,"//span[2]")
print("Location of the Slider before moving........")
print(min_slider.location) #{'x': 59, 'y': 250}
print(max_slider.location)  #{'x': 510, 'y': 250}
act.drag_and_drop_by_offset(min_slider,109,250).perform()
act.drag_and_drop_by_offset(max_slider,-59,250).perform()

print("loaction after slider moving......")
print(max_slider.location) #{'x': 486, 'y': 250}
print(min_slider.location) #{'x': 171, 'y': 250}



