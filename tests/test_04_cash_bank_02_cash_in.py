import os
import pytest

from pages.login_page import LoginPage
from pages.cash_in_page import CashInPage
from utils.helper import clear_and_fill, set_select_value

 

def test_create_Cash_In_success(driver):
    login_page = LoginPage(driver)
    cash_in_page = CashInPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # login
    login_page.open(base_url)
    login_page.login(email, password)

    # ke Cash In page
    cash_in_page.go_to_cash_in()

    # create Cash In
    cash_in_page.click_create()
    cash_in_page.set_txn_date_today()
    code = cash_in_page.fill_form_random(1)
    cash_in_page.submit() 