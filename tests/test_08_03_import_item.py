import os
import pytest


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.login_page import LoginPage
from pages.import_items_page import ImportItemsPage



def test_import_items_wrong_header(driver):
    login_page = LoginPage(driver)
    import_items_page = ImportItemsPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_items_page.go_to_import_menu()
    import_items_page.go_to_import_item()

    # UPLOAD FILE SALAH
    import_items_page.upload_xls("data/master_wrong_header.xls")
    import_items_page.submit()

    # VALIDASI ALERT
    alert_message = import_items_page.get_error_alert_message()
    assert "Kolom header harus ada: code, sku, name, uom_code, item_type, is_active" in alert_message



def test_import_items_success(driver):
    login_page = LoginPage(driver)
    import_items_page = ImportItemsPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_items_page.go_to_import_menu()
    import_items_page.go_to_import_item()

    # UPLOAD XLS SALAH
    import_items_page.upload_xls("data/master_items.xls")
    import_items_page.submit()

    # VALIDASI ALERT
    WebDriverWait(driver, 10).until(
        EC.url_contains("/master/items")
    )

    assert "/master/items" in driver.current_url 