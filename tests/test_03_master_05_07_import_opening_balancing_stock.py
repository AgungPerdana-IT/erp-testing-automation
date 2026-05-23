import os
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.import_opening_balancing_stock_page import ImportBalancingStockPage



def test_import_balancing_stock_wrong_header(driver):
    login_page = LoginPage(driver)
    import_balancing_stock_page = ImportBalancingStockPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_balancing_stock_page.go_to_import_menu()
    import_balancing_stock_page.go_to_import_opening_balancing_stock()

    # PILIH TANGGAL
    import_balancing_stock_page.set_txn_date_today()

    # UPLOAD FILE SALAH
    import_balancing_stock_page.upload_xls("data/master_wrong_header.xls")
    import_balancing_stock_page.submit()

    # VALIDASI ALERT
    alert_message = import_balancing_stock_page.get_error_alert_message()
    assert "Header CSV required punya kolom sku or code (item identifier)." in alert_message


def test_import_balancing_stock_success(driver):
    login_page = LoginPage(driver)
    import_balancing_stock_page = ImportBalancingStockPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_balancing_stock_page.go_to_import_menu()
    import_balancing_stock_page.go_to_import_opening_balancing_stock()

    # PILIH TANGGAL
    import_balancing_stock_page.set_txn_date_today()

    # UPLOAD FILE BENAR
    import_balancing_stock_page.upload_xls("data/opening_stock.xls")
    import_balancing_stock_page.submit()

    # VALIDASI ALERT
    WebDriverWait(driver, 10).until(
        EC.url_contains("/finance/stock-invoices")
    )

    assert "/finance/stock-invoices" in driver.current_url