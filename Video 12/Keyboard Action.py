from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

#Ctrl+A=
#Ctrl+C=
#Tab
#Ctrl+V

serv_obj = Service("C:/Users/BHANU/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.get("https://text-compare.com/")
driver.maximize_window()
input1 = driver.find_element(By.XPATH,"//*[@id='inputText1']")
input2 = driver.find_element(By.XPATH,"//*[@id='inputText2']")
input1.send_keys("Welcome to Python with Selenium")
act = ActionChains(driver)
# act.key_down(keys.Control)
# act.send_keys("a")
# act.key_up(keys.Control)
# act.perform()
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
