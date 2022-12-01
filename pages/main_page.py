import time
import pytest
from .locators import MainPageLocators
from .Base_page import BasePage


class MainPage(BasePage):

    def choice_by_filter(self):
        filter_by_type = self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE)
        filter_by_type.click()
        dog = self.browser.find_element(*MainPageLocators.DOG)
        dog.click()
        filter_by_pet_name = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_NAME)
        filter_by_pet_name.send_keys('Bob')
        logo = self.browser.find_element(*MainPageLocators.LOGO)
        logo.click()
        details = self.browser.find_element(*MainPageLocators.DETAILS)
        details.click()
        comments = self.browser.find_element(*MainPageLocators.COMMENTS)
        comments.send_keys('Very nice doggy')

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_registration_page(self):
        register_link = self.browser.find_element(*MainPageLocators.REGISTER_LINK)
        register_link.click()

    def pagination(self):
        third_page = self.browser.find_element(*MainPageLocators.THIRD_PAGE)
        third_page.click()
        time.sleep(3)


    def like(self):
        like_for_first_pet = self.browser.find_element(*MainPageLocators.LIKE_FOR_FIRST_PET)
        like_for_first_pet.click()
        time.sleep(3)

    def watch_foto(self):
        details_of_first_pet = self.browser.find_element(*MainPageLocators.DETAILS_FIST_PET)
        details_of_first_pet.click()
        watch_foto = self.browser.find_element(*MainPageLocators.PREWIEW_FOTO_OF_FIRST_PET)
        watch_foto.click()
        time.sleep(3)
