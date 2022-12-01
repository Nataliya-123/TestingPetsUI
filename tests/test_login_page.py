from pages.login_page import LoginPage
import pytest
from pages.local_setting import url_login_page


@pytest.mark.smoke
def test_go_to_login(browser):
    link = url_login_page
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()



@pytest.mark.regression
def test_go_to_icon(browser):
    link = url_login_page
    page = LoginPage(browser, link)
    page.open()
    page.go_to_icon()
