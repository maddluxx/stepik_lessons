from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math


basket_init_price = ["0,00", "0.00", "£0.00", "0,00 £", "0,00 GBP", "0,00 £GB"]


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def go_to_catalogue_page(self):
        link = self.browser.find_element(*BasePageLocators.CATALOGUE_LINK)
        link.click()

    def go_to_next_catalogue_page(self):
        link = self.browser.find_element(*BasePageLocators.NEXT_PAGE)
        link.click()

    def should_have_product(self):
        assert self.is_element_present(*BasePageLocators.PRODUCT), "No products found."

    def should_be_zero_init_price_in_basket(self):
        basket_price_value = \
            self.browser.find_element(*BasePageLocators.BASKET_MINI).text.split(':')[1].split('\n')[0].strip()
        assert basket_price_value in basket_init_price, \
            f"Expected \"{basket_init_price}\" for initial basket price, got \"{basket_price_value}\""

    def add_first_available_item_to_basket(self):
        add_to_basket_button = self.browser.find_element(*BasePageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def add_second_available_item_to_basket(self):
        add_to_basket_button = self.browser.find_elements(*BasePageLocators.ADD_TO_BASKET_BUTTON)[1]
        add_to_basket_button.click()

    def should_match_price_in_basket_and_alert(self):
        alert_price_value = self.browser.find_element(*BasePageLocators.BASKET_UPDATE_ALERT).text
        basket_price_value = \
            self.browser.find_element(*BasePageLocators.BASKET_MINI).text.split(':')[1].split('\n')[0].strip()
        assert alert_price_value == basket_price_value, \
            f"Price in the alert and price in the basket should match. Got alert_price_value={alert_price_value} and " \
            f"basket_price_value={basket_price_value} instead"
