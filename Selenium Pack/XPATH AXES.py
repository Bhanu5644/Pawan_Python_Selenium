from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select

serv_obj=Service("C:/Users/BHANU/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
# XPATH AXES (Not use mostly but we need to know)
# Self element
Text = driver.find_element(By.XPATH,"//a[normalize-space()='Maruti Infrastru']/self::a").text
print(Text)
#Parent
# Text = driver.find_element(By.XPATH,"//a[contains(.,'Suyog Telematics')]/parent::td").text
# print(Text)
#Child
# Childs = driver.find_element(By.XPATH,"//a[contains(.,'Suyog Telematics')]/ancestor::tr/child::tr").text
# print(len(Childs))
#Ancestor
# Text = driver.find_element(By.XPATH,"//a[contains(.,'Suyog Telematics')]/ancestor::td").text
# print(Text) #Entire row data will written
# #Decendant
# Decendant = driver.find_element(By.XPATH,"//a[contains(.,'Suyog Telematics')]/decendant::*").text
# print("Number of decendant node:",len(Decendant)) #7
#
# #Following
# Following = driver.find_element(By.XPATH,"//a[contains(.,'Suyog Telematics')]/following::*").text
# print("Number of decendant node:",len(following)) #7
#
# #Following-Sibling:
# FollowingSibling = driver.find_element(By.XPATH,"//a[contains(.,'Suyog Telematics')]/ancestor::tr/following-sibling::tr").text
# print("Number of decendant node:",len(FollowingSibling)) #7
#
# #preceding:
# preceding = driver.find_element(By.XPATH,"//a[contains(.,'Suyog Telematics')]/ancestor::tr/preceding::tr").text
# print("Number of decendant node:",len(preceding)) #7
#
# #preceding-Sibling:
# precedingsibling = driver.find_element(By.XPATH,"//a[contains(.,'Suyog Telematics')]/ancestor::tr/preceding-sibling::tr").text
# print("Number of decendant node:",len(precedingsibling)

