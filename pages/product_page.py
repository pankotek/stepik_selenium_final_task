from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_CART_MESSAGES), \
            "Success message is presented, but should not be"

    def success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_CART_MESSAGES), \
            "Success message is presented, but should not be"
