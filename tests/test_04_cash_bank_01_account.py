import os
import pytest

from pages.login_page import LoginPage
from pages.accounts_page import AccountPage
from utils.helper import clear_and_fill, set_select_value

 

def test_create_account_success(driver):
    login_page = LoginPage(driver)
    accounts_page = AccountPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # login
    login_page.open(base_url)
    login_page.login(email, password)

    # ke Accounts page
    accounts_page.go_to_accounts()

    # create Account
    accounts_page.click_create()
    code = accounts_page.fill_form_random(1)
    accounts_page.submit()