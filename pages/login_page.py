from .Base_page import BasePage
from .locators import LoginPageLocator
from .local_setting import login
from .local_setting import password


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocator.LOGIN_EMAIL)
        login_email.send_keys(login)

        login_password = self.browser.find_element(*LoginPageLocator.LOGIN_PASSWORD)
        login_password.send_keys(password)

        login_button = self.browser.find_element(*LoginPageLocator.LOGIN_BTN)
        login_button.submit()

    def go_to_icon(self):
        icon = self.browser.find_element(*LoginPageLocator.ICON)
        icon.click()
