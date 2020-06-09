from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > .price_color")
    PRODUCT_ADDED_NAME = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_ADDED_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    ADD_TO_CART_MESSAGES = (By.CSS_SELECTOR, "div#messages div.alertinner")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, 'a[href$="basket/"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_NOT_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
