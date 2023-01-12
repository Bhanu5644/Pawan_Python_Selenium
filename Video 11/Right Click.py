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
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
act = ActionChains(driver)
button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
act.context_click(button).perform() # Right Click
driver.find_element(By.XPATH,"/html/body/ul/li[3]").click()
time.sleep(5)
driver.switch_to.alert.accept()