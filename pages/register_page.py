from .locators import RegisterPageLocator
from .Base_page import BasePage
from .local_setting import login_for_registration
from .local_setting import password


class RegisterPage(BasePage):
    def registration_and_delete_profile(self):
        login_button = self.browser.find_element(*RegisterPageLocator.LOGIN_BUTTON)
        login_button.send_keys(login_for_registration)
        password_button = self.browser.find_element(*RegisterPageLocator.PASSWORD_BUTTON)
        password_button.send_keys(password)

        confirm_password = self.browser.find_element(*RegisterPageLocator.CONFIRM_PASSWORD_BUTTON)
        confirm_password.submit()
        confirm_password.send_keys(password)
        submit_button = self.browser.find_element(*RegisterPageLocator.SUBMIT_BUTTON)
        submit_button.submit()
        delete_profile = self.browser.find_element(*RegisterPageLocator.DELETE_BTN)
        delete_profile.click()
        yes_delete = self.browser.find_element(*RegisterPageLocator.YES_BTN_POPUP)
        yes_delete.click()
