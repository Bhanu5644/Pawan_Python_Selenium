from lib2to3.pgen2 import driver

import pytest
from selenium.webdriver.common.by import
from selenium.webdriver.support.wait import
from selenium.webdriver.support import

@pytest.mark.usefixtures("setup")
class TestOne:

    def test_e2e(self):


        driver.find_element_by_css_selector("a[href*='shop'").click()
        card = driver.find_element_by_css_selector(".card-title a")
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.test
            print(cardText)
            if cardText == "Blackberry":
