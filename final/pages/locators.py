from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_MINI = (By.CSS_SELECTOR, ".basket-mini")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    BASKET_UPDATE_ALERT = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")
    CATALOGUE_LINK = (By.CSS_SELECTOR, "#browse .dropdown-menu li a")
    PRODUCT = (By.CSS_SELECTOR, ".product_pod")
    NEXT_PAGE = (By.CSS_SELECTOR, ".pager a")


class BasketPageLocators():
    BASKET_CONTENT_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_ITEMS_TOTALS = (By.CSS_SELECTOR, ".col-sm-2 .price_color.align-right")
    BASKET_TOTAL_WITHOUT_DISCOUNTS = (By.CSS_SELECTOR, "#basket_totals .align-right")
    BASKET_TOTALS = (By.CSS_SELECTOR, "#basket_totals .total.align-right")
    DELETE_ITEM = (By.CSS_SELECTOR, ".basket-items .inline")
    ITEM_TITLE = (By.CSS_SELECTOR, ".basket-items h3 a")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    CHECKOUT_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_username")
    CHECKOUT_NEW_USER_TOGGLE = (By.CSS_SELECTOR, "#id_options_0")
    CHECKOUT_DELIVERY_FORM = (By.CSS_SELECTOR, ".shipping-payment")
    CHECKOUT_FIRST_NAME = (By.CSS_SELECTOR, "#id_first_name")
    CHECKOUT_LAST_NAME = (By.CSS_SELECTOR, "#id_last_name")
    CHECKOUT_ADDRESS = (By.CSS_SELECTOR, "#id_line1")
    CHECKOUT_CITY = (By.CSS_SELECTOR, "#id_line4")
    CHECKOUT_ZIP_CODE = (By.CSS_SELECTOR, "#id_postcode")
    CHECKOUT_COUNTRY = (By.CSS_SELECTOR, "#id_country")
    CHECKOUT_PAYPAL_OPTION = (By.CSS_SELECTOR, ".page_inner li a")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form button")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    BASKET = (By.CSS_SELECTOR, ".basket-mini")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
