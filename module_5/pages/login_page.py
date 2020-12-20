from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL does not include 'login' in it"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self, email, password):
        reg_email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        reg_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        reg_password_confirmation_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        reg_submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        reg_email_field.send_keys(email)
        reg_password_field.send_keys(password)
        reg_password_confirmation_field.send_keys(password)
        reg_submit_button.click()
