from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_items_in_basket()
        self.should_be_empty_basket_message()

    def should_not_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Products added to the basket but should not be"

    def should_be_empty_basket_message(self):
        assert "Your basket is empty" in self.browser.find_element(
            *BasketPageLocators.BASKET_CONTENT_TEXT).text, \
            "'Your basket is empty' message is not found"
