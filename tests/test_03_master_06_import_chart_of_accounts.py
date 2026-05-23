import os
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.import_chart_of_accounts_page import ImportChartOfAccountPage


def test_import_chart_of_account_wrong_header(driver):
    login_page = LoginPage(driver)
    import_chart_of_accounts_page = ImportChartOfAccountPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_chart_of_accounts_page.go_to_import_menu()
    import_chart_of_accounts_page.go_to_import_chart_of_account()

    # UPLOAD FILE SALAH
    import_chart_of_accounts_page.upload_xls("data/master_wrong_header.xls")
    import_chart_of_accounts_page.submit()

    # VALIDASI ALERT
    alert_message = import_chart_of_accounts_page.get_error_alert_message()
    assert "Kolom header harus ada: code, name, type, is_active" in alert_message



def test_import_chart_of_account_succses(driver):
    login_page = LoginPage(driver)
    import_chart_of_accounts_page = ImportChartOfAccountPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_chart_of_accounts_page.go_to_import_menu()
    import_chart_of_accounts_page.go_to_import_chart_of_account()

    # UPLOAD FILE BENAR
    import_chart_of_accounts_page.upload_xls("data/master_coa.xls")
    import_chart_of_accounts_page.submit()

    # VALIDASI ALERT
    WebDriverWait(driver, 10).until(
        EC.url_contains("/master/coa")
    )

    assert "/master/coa" in driver.current_url