from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY)

    def basket_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_NOT_EMPTY_TEXT)