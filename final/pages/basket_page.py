from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.support.ui import Select
import re
import time


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

    def should_have_correct_totals_without_discount(self):
        items_total_price = 0.0
        for item_total_price in self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS_TOTALS):
            item_total_price_cleaned = re.sub("[^0-9,.]", "", item_total_price.text)
            item_total_price_cleaned = re.sub("[,]", ".", item_total_price_cleaned)
            items_total_price += float(item_total_price_cleaned)
        items_total_price = round(items_total_price, 2)
        basket_total_price_without_discounts = re.sub("[^0-9,.]", "",
                                                      self.browser.find_element(
                                                          *BasketPageLocators.BASKET_TOTAL_WITHOUT_DISCOUNTS).text)
        basket_total_price_without_discounts = float(re.sub("[,]", ".", basket_total_price_without_discounts))
        assert items_total_price == basket_total_price_without_discounts, \
            f"Calculated {items_total_price} but got {basket_total_price_without_discounts}"

    def should_have_correct_totals(self):
        basket_total = re.sub("[^0-9,.-]", "", self.browser.find_elements(*BasketPageLocators.BASKET_TOTALS)[0].text)
        basket_total = float(re.sub("[,]", ".", basket_total))
        delivery_price = re.sub("[^0-9,.-]", "", self.browser.find_elements(*BasketPageLocators.BASKET_TOTALS)[1].text)
        delivery_price = float(re.sub("[,]", ".", delivery_price))
        total_result = re.sub("[^0-9,.-]", "", self.browser.find_elements(*BasketPageLocators.BASKET_TOTALS)[2].text)
        total_result = float(re.sub("[,]", ".", total_result))
        assert (basket_total + delivery_price) == total_result, "Totals with discounts do not match"

    def should_delete_item(self):
        item_to_delete = self.browser.find_element(*BasketPageLocators.ITEM_TITLE).text
        link = self.browser.find_element(*BasketPageLocators.DELETE_ITEM)
        link.click()
        item_left = self.browser.find_element(*BasketPageLocators.ITEM_TITLE).text
        assert item_to_delete != item_left, "Failed to delete an item from the basket."

    def go_to_checkout(self):
        link = self.browser.find_element(*BasketPageLocators.CHECKOUT_BUTTON)
        link.click()

    def fill_guest_checkout_form(self):
        email = str(time.time()) + "@fakemail.org"
        checkout_email_field = self.browser.find_element(*BasketPageLocators.CHECKOUT_EMAIL_FIELD)
        checkout_email_field.send_keys(email)
        checkout_new_user_toggle = self.browser.find_element(*BasketPageLocators.CHECKOUT_NEW_USER_TOGGLE)
        checkout_new_user_toggle.click()
        checkout_button = self.browser.find_element(*BasketPageLocators.CHECKOUT_BUTTON)
        checkout_button.click()

    def should_be_delivery_form(self):
        assert self.is_element_present(*BasketPageLocators.CHECKOUT_DELIVERY_FORM), "Delivery form is not found."

    def fill_user_delivery_form(self):
        first_name = self.browser.find_element(*BasketPageLocators.CHECKOUT_FIRST_NAME)
        first_name.send_keys(str(time.time()) + "_first_name")
        last_name = self.browser.find_element(*BasketPageLocators.CHECKOUT_LAST_NAME)
        last_name.send_keys(str(time.time()) + "_last_name")
        address = self.browser.find_element(*BasketPageLocators.CHECKOUT_ADDRESS)
        address.send_keys("Ulice")
        city = self.browser.find_element(*BasketPageLocators.CHECKOUT_CITY)
        city.send_keys("Praha")
        zip = self.browser.find_element(*BasketPageLocators.CHECKOUT_ZIP_CODE)
        zip.send_keys("17000")
        country = Select(self.browser.find_element(*BasketPageLocators.CHECKOUT_COUNTRY))
        country.select_by_value("CZ")

    def should_be_payment_form(self):
        assert "paypal" in self.browser.find_element(*BasketPageLocators.CHECKOUT_PAYPAL_OPTION).text, \
            "Payment form is not found."

    def should_be_preview_url(self):
        assert "preview" in self.browser.current_url, "URL does not include 'preview' in it"

    def should_be_thank_you_url(self):
        assert "thank-you" in self.browser.current_url, "URL does not include 'thank-you' in it"
