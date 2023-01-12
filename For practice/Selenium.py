from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# service_obj= Service("C:\Users\BHANU\Documents\chromedriver_win32.exe");
driver = webdriver.Chrome("C:\\Users\BHANU\Documents\chromedriver_win32\chromedriver.exe")
driver.get("http://www.amazon.in")
driver.maximize_window()
time.sleep(5)
driver.close()