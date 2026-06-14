import os
import pytest

from pages.login_page import LoginPage
from pages.ledger_page import LedgerPage
from utils.helper import clear_and_fill, set_select_value

 

def test_create_Ledger_success(driver):
    login_page = LoginPage(driver)
    ledger_page = LedgerPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # login
    login_page.open(base_url)
    login_page.login(email, password)

    # ke Ledger page
    ledger_page.go_to_ledger()
