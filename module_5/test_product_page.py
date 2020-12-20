from .pages.product_page import ProductPage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


class TestProductPage:
    # @pytest.mark.parametrize('link',
    #                          ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    #                           pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    # def test_guest_can_add_product_to_basket(self, browser, link):
    #     # Arrange
    #     #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #     #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #     #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
    #     page = ProductPage(browser, link)
    #     page.open()
    #     #page.should_not_be_success_message()
    #     page.arrange_prerequisites()
    #     # Act
    #     page.add_product_to_basket()
    #     # Assert
    #     page.should_be_success_message()
    #     page.should_be_correct_product_in_success_message()
    #     page.should_be_basket()
    #     page.should_be_correct_price_in_basket()
    #     #time.sleep(60)

    @pytest.mark.xfail(reason="wrong test")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.add_product_to_basket()
        # Assert
        page.should_not_be_success_message()
        # time.sleep(1)

    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Assert
        page.should_not_be_success_message()
        # time.sleep(1)

    @pytest.mark.xfail(reason="not implemented yet")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.add_product_to_basket()
        # Assert
        page.should_disappear_success_message()
        # time.sleep(1)