import time
import pytest
from pages.main_page import MainPage
from pages.local_setting import url_main_page
from pages.local_setting import url_login_page

@pytest.mark.smoke
def test_choice_by_filter(browser):
    link = url_main_page
    page = MainPage(browser, link)
    page.open()
    page.choice_by_filter()
    time.sleep(3)


@pytest.mark.smoke
def test_go_to_login_page(browser):
    link = url_main_page
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    screenshot = browser.save_screenshot('result.png')
    current_url = browser.current_url
    assert screenshot
    assert current_url == url_login_page


@pytest.mark.smoke
def test_go_to_registration_page(browser):
    link = url_main_page
    page = MainPage(browser, link)
    page.open()
    page.go_to_registration_page()


@pytest.mark.regression
def test_pagination(browser):
    link = url_main_page
    page = MainPage(browser, link)
    page.open()
    page.pagination()


@pytest.mark.xfail
def test_like(browser):
    link = url_main_page
    page = MainPage(browser, link)
    page.open()
    page.like()


@pytest.mark.regression
def test_watch_foto(browser):
    link = url_main_page
    page = MainPage(browser, link)
    page.open()
    page.watch_foto()
