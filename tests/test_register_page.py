import time
from pages.register_page import RegisterPage
from pages.local_setting import url_register_page
import pytest


@pytest.mark.xfail
def test_registration_and_delete_profile(browser):
    link = url_register_page
    page = RegisterPage(browser, link)
    page.open()
    page.registration_and_delete_profile()
    time.sleep(3)


