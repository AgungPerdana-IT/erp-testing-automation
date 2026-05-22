import os
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.import_price_list_lines_page import ImportPriceListLinesPage



def test_import_price_list_lines_wrong_header(driver):
    login_page = LoginPage(driver)
    import_price_list_lines_page = ImportPriceListLinesPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_price_list_lines_page.go_to_import_menu()
    import_price_list_lines_page.go_to_import_price_list_lines()

    # UPLOAD FILE SALAH
    import_price_list_lines_page.upload_xls("data/master_wrong_header.xls")
    import_price_list_lines_page.submit()

    # VALIDASI ALERT
    alert_message = import_price_list_lines_page.get_error_alert_message()
    assert "Kolom header harus ada: pricelist_code, item_code, uom_code, price, valid_from" in alert_message


def test_import_price_list_lines_success(driver):
    login_page = LoginPage(driver)
    import_price_list_lines_page = ImportPriceListLinesPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_price_list_lines_page.go_to_import_menu()
    import_price_list_lines_page.go_to_import_price_list_lines()

    # UPLOAD XLS SALAH
    import_price_list_lines_page.upload_xls("data/price_list_lines.xls")
    import_price_list_lines_page.submit()

    # VALIDASI ALERT
    WebDriverWait(driver, 10).until(
        EC.url_contains("/master/price-lists")
    )

    assert "/master/price-lists" in driver.current_url 