import os
from pages.import_chart_of_accounts_page import ImportChartOfAccountPage
import pytest

from pages.login_page import LoginPage
from pages.reconciliation_page import ReconciliationPage
from utils.helper import clear_and_fill, set_select_value

 

def test_import_reconciliation_wrong_header(driver):
    login_page = LoginPage(driver)
    reconciliation_page = ReconciliationPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    reconciliation_page.go_to_reconciliation()

    # UPLOAD FILE SALAH
    reconciliation_page.fill_form_random(0)
    reconciliation_page.filter()
    reconciliation_page.upload_xls("data/master_wrong_header.xls")
    reconciliation_page.preview()

    # VALIDASI PREVIEW
    alert_message = reconciliation_page.get_error_alert_message()
    assert "No valid rows to import. 2 row(s) are invalid." in alert_message
    



def test_import_reconciliation_success(driver):
    login_page = LoginPage(driver)
    reconciliation_page = ReconciliationPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    reconciliation_page.go_to_reconciliation()

    # UPLOAD FILE BENAR
    reconciliation_page.fill_form_random(0)
    reconciliation_page.filter()
    reconciliation_page.upload_xls("data/bank-statement-template.xlsx")
    reconciliation_page.preview()

    # VALIDASI PREVIEW
    assert "/cash-bank/reconcile/preview" in driver.current_url

    reconciliation_page.submit()

    # VALIDASI ALERT
    assert "/cash-bank/reconcile" in driver.current_url