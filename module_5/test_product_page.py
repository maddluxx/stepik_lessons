from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


class TestProductPage:
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        # Arrange
        #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
        page = ProductPage(browser, link)
        page.open()
        #page.should_not_be_success_message()
        page.arrange_prerequisites()
        # Act
        page.add_product_to_basket()
        # Assert
        page.should_be_success_message()
        page.should_be_correct_product_in_success_message()
        page.should_be_basket()
        page.should_be_correct_price_in_basket()
        #time.sleep(60)

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

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()

    class TestUserAddToBasketFromProductPage():
        @pytest.fixture(scope="function", autouse=True)
        def setup(self, browser):
            page = ProductPage(browser, link)
            page.open()
            page.go_to_login_page()
            login_page = LoginPage(browser, browser.current_url)
            email = str(time.time()) + "@fakemail.org"
            login_page.register_new_user(email=email, password=email)
            login_page.should_be_authorized_user()

        def test_user_cant_see_success_message(self, browser):
            # Arrange
            page = ProductPage(browser, link)
            page.open()
            # Assert
            page.should_not_be_success_message()
            # time.sleep(1)

        def test_user_can_add_product_to_basket(self, browser):
            # Arrange
            #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
            #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
            #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
            page = ProductPage(browser, link)
            page.open()
            #page.should_not_be_success_message()
            page.arrange_prerequisites()
            # Act
            page.add_product_to_basket()
            # Assert
            page.should_be_success_message()
            page.should_be_correct_product_in_success_message()
            page.should_be_basket()
            page.should_be_correct_price_in_basket()
            #time.sleep(60)
