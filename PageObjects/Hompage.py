from selenium.webdriver.common.by import By


class homepage:

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItem(self):
        driver.find_element(*HomePage.shop)