from .pages.product_page import ProductPage
import time


link = "http://selenium1py.pythonanywhere.com/"


class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser):
        # Arrange
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.arrange_prerequisites()
        # Act
        page.add_product_to_basket()
        # Assert
        page.should_be_success_message()
        page.should_be_correct_product_in_success_message()
        page.should_be_basket()
        page.should_be_correct_price_in_basket()
        time.sleep(10)
