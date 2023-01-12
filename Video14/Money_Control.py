from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from Video14 import XLutility
import time

serv_obj=Service("C:/Users/BHANU/Downloads/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/indus-ind-bank/fixed-deposit-calculator-IIB-BII001.html?classic=true")
driver.maximize_window()

File = "C:/Users/BHANU/OneDrive/Money Control.xls"
row = XLutility.getRowCount(File,"Sheet1")
#Reading Data
for r in range(2,row+1):
    Principle = XLutility.readData(File,"Sheet1",r,1)
    Rateofintrest = XLutility.readData(File,"Sheet1", r,2)
    Period1 = XLutility.readData(File,"Sheet1", r,3)
    Period2 = XLutility.readData(File,"Sheet1", r,4)
    Frequency = XLutility.readData(File, "Sheet1", r,5)
    Maturity = XLutility.readData(File, "Sheet1", r,6)
    #Pass data in Application
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(Principle)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(Rateofintrest)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(Period1)
    perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(Period2)
    frequencydrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frequencydrp.select_by_visible_text(Frequency)
    driver.find_element(By.XPATH, "//*[@id='wzrk-confirm']").click()

    driver.find_element(By.XPATH,"//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
    act_mvalue=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text
    if float(Maturity) == float(act_mvalue):
        print("Test Pass")
        XLutility.writeData(File,"Sheet1",r,8,"Pass")
        XLutility.fillGreenColor(File,"Sheet1",r,8)
    else:
        print("Test Fail")
        XLutility.writeData(File,"Sheet1",r,8,"fail")
        XLutility.fillRedColor(File,"Sheet1",r,8)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    driver.close()


