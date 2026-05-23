import os
import pytest

from pages.login_page import LoginPage
from pages.cash_out_page import CashOutPage
from utils.helper import clear_and_fill, set_select_value

 

def test_create_Cash_Out_success(driver):
    login_page = LoginPage(driver)
    cash_out_page = CashOutPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # login
    login_page.open(base_url)
    login_page.login(email, password)

    # ke Cash Out page
    cash_out_page.go_to_cash_out_menu()

    # create Cash Out
    cash_out_page.click_create()
    cash_out_page.set_txn_date_today()
    code = cash_out_page.fill_form_random(1)
    cash_out_page.submit() 