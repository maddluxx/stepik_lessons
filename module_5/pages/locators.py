from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn.btn-default")


class BasketPageLocators():
    BASKET_CONTENT_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


#class MainPageLocators():
#    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    BASKET = (By.CSS_SELECTOR, ".basket-mini")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
