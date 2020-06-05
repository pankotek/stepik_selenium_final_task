from .pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    name = page.get_name()
    price = page.get_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.assert_name(name)
    page.assert_price(price)


# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.success_message_disappeared()
