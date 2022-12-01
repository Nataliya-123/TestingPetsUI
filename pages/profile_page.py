import time

from .Base_page import BasePage
from .locators import ProfilePageLocator
from .locators import LoginPageLocator

from .local_setting import login
from .local_setting import password

class LoginPage(BasePage):
    def go_to_login(self):
        login_email= self.browser.find_element(*LoginPageLocator.LOGIN_EMAIL)
        login_email.send_keys(login)

        login_password = self.browser.find_element(*LoginPageLocator.LOGIN_PASSWORD)
        login_password.send_keys(password)

        login_button = self.browser.find_element(*LoginPageLocator.LOGIN_BTN)
        login_button.submit()

class ProfilePage(BasePage):
    def add_new_pet(self):
        plus_button = self.browser.find_element(*ProfilePageLocator.PLUS_BUTTON)
        plus_button.click()
        name_new_pet = self.browser.find_element(*ProfilePageLocator.NAME_NEW_PET)
        name_new_pet.send_keys('Bobik')
        type_of_pet = self.browser.find_element(*ProfilePageLocator.SELECT_A_TYPE)
        type_of_pet.click()
        select_type_of_new_pet = self.browser.find_element(*ProfilePageLocator.TYPE_OF_NEW_PET)
        select_type_of_new_pet.click()
        age = self.browser.find_element(*ProfilePageLocator.AGE)
        age.send_keys(2)
        gender= self.browser.find_element(*ProfilePageLocator.SELECT_A_GENDER)
        gender.click()
        male = self.browser.find_element(*ProfilePageLocator.MALE)
        male.click()
        submit_new_pet = self.browser.find_element(*ProfilePageLocator.SUBMIT_NEW_PET)
        submit_new_pet.click()

    def cancel_add_new_pet(self):
        plus_button = self.browser.find_element(*ProfilePageLocator.PLUS_BUTTON)
        plus_button.click()
        name_new_pet = self.browser.find_element(*ProfilePageLocator.NAME_NEW_PET)
        name_new_pet.send_keys('Bobik')
        type_of_pet = self.browser.find_element(*ProfilePageLocator.SELECT_A_TYPE)
        type_of_pet.click()
        select_type_of_new_pet = self.browser.find_element(*ProfilePageLocator.TYPE_OF_NEW_PET)
        select_type_of_new_pet.click()
        age = self.browser.find_element(*ProfilePageLocator.AGE)
        age.send_keys(2)
        gender = self.browser.find_element(*ProfilePageLocator.SELECT_A_GENDER)
        gender.click()
        male = self.browser.find_element(*ProfilePageLocator.MALE)
        male.click()
        cancel_add_new_pet = self.browser.find_element(*ProfilePageLocator.CANCEL_NEW_PET)
        cancel_add_new_pet.click()

    def delete(self):
        delete = self.browser.find_element(*ProfilePageLocator.DELETE)
        delete.click()
        popap_yes = self.browser.find_element(*ProfilePageLocator.POPAP_YES)
        popap_yes.click()

    def edit(self):
        edit = self.browser.find_element(*ProfilePageLocator.EDIT)
        edit.click()
        edit_name = self.browser.find_element(*ProfilePageLocator.NAME)
        edit_name.click()
        time.sleep(2)
        edit_name.clear()
        edit_name.send_keys('223')
        time.sleep(2)
        save_edit = self.browser.find_element(*ProfilePageLocator.SAVE_EDIT)
        save_edit.click()
        time.sleep(2)

    def quit(self):
        quit = self.browser.find_element(*ProfilePageLocator.QUIT)
        quit.click()











