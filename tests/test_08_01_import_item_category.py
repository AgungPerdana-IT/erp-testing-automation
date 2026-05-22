import os
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.import_item_categories_page import ImportItemCategoriesPage


def test_import_item_categories_wrong_header(driver):
    login_page = LoginPage(driver)
    import_item_categories_page = ImportItemCategoriesPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_item_categories_page.go_to_import_menu()
    import_item_categories_page.go_to_import_item_categories()

    # UPLOAD FILE SALAH
    import_item_categories_page.upload_xls("data/master_wrong_header.xls")
    import_item_categories_page.submit()

    # VALIDASI ALERT
    alert_message = import_item_categories_page.get_error_alert_message()
    assert "Kolom header harus ada: code, name, is_active" in alert_message


def test_import_item_categories_success(driver):
    login_page = LoginPage(driver)
    import_item_categories_page = ImportItemCategoriesPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_item_categories_page.go_to_import_menu()
    import_item_categories_page.go_to_import_item_categories()

    # UPLOAD XLS BENAR
    import_item_categories_page.upload_xls("data/master_item_categories.xls")
    import_item_categories_page.submit()

    # VALIDASI ALERT
    WebDriverWait(driver, 10).until(
        EC.url_contains("/master/item-categories")
    )

    assert "/master/item-categories" in driver.current_url