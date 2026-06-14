import os
import pytest

from pages.login_page import LoginPage
from pages.transfer_page import TransfersPage
from utils.helper import clear_and_fill, set_select_value

 

def test_create_Transfer_success(driver):
    login_page = LoginPage(driver)
    transfers_page = TransfersPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # login
    login_page.open(base_url)
    login_page.login(email, password)

    # ke Transfers page
    transfers_page.go_to_transfers_menu()

    # create Transfer
    transfers_page.click_create()
    transfers_page.set_txn_date_today()
    code = transfers_page.fill_form_random(1)
    transfers_page.submit() 