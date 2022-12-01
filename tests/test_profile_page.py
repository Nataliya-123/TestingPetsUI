import time
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.local_setting import url_login_page
from pages.local_setting import url_profile_page
import pytest


def test_add_new_pet(browser):
    link = url_login_page
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    time.sleep(3)
    link = url_profile_page
    page = ProfilePage(browser, link)
    page.open()
    page.add_new_pet()
    time.sleep(3)


@pytest.mark.regression
@pytest.mark.smoke
def test_cancel_add_new_pet(browser):
    link = url_login_page
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    time.sleep(3)
    link = url_profile_page
    page = ProfilePage(browser, link)
    page.open()
    page.cancel_add_new_pet()
    time.sleep(3)


@pytest.mark.smoke
def test_delete(browser):
    link = url_login_page
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    time.sleep(3)
    link = url_profile_page
    page = ProfilePage(browser, link)
    page.open()
    page.delete()
    time.sleep(3)


@pytest.mark.smoke
def test_edit(browser):
    link = url_login_page
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    time.sleep(3)
    link = url_profile_page
    page = ProfilePage(browser, link)
    page.open()
    page.edit()
    time.sleep(3)


@pytest.mark.skip
@pytest.mark.regression
def test_quit(browser):
    link = url_login_page
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    time.sleep(3)
    link = url_profile_page
    page = ProfilePage(browser, link)
    page.open()
    page.quit()
