from selenium.webdriver.chrome import webdriver
from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def Setup():

    driver = webdriver.Chrome(executable_path="C:\\Users\BHANU\Documents\chromedriver_win32\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
