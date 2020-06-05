from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def add_to_basket(self):
        name = self.get_name()
        price = self.get_price()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()
        self.assert_name(name)
        self.assert_price(price)

    def get_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def assert_name(self, name):
        added_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_NAME).text
        assert added_name == name, "Name is incorrect"

    def assert_price(self, price):
        added_price = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_PRICE).text
        assert added_price == price, "Price is incorrect"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
