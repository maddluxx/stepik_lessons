from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def arrange_prerequisites(self):
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is present but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared but it should"

    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not present"

    def should_be_correct_product_in_success_message(self):
        assert self.product_name == self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text, \
            "Success message do not have correct product name in it"

    def should_be_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET), "Basket is not present"

    def should_be_correct_price_in_basket(self):
        assert self.product_price in self.browser.find_element(
            *ProductPageLocators.BASKET).text, "Basket price does not match product price"
