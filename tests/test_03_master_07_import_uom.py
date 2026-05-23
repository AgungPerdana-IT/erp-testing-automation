import os
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.import_uoms_page import ImportUomsPage


def test_import_uom_wrong_header(driver):
    login_page = LoginPage(driver)
    import_uoms_page = ImportUomsPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_uoms_page.go_to_import_menu()
    import_uoms_page.go_to_import_uom()

    # UPLOAD FILE SALAH
    import_uoms_page.upload_xls("data/master_wrong_header.xls")
    import_uoms_page.submit()

    # VALIDASI ALERT
    alert_message = import_uoms_page.get_error_alert_message()
    assert "Kolom header harus ada: code, name, is_active" in alert_message




def test_import_uom_succses(driver):
    login_page = LoginPage(driver)
    import_uoms_page = ImportUomsPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_uoms_page.go_to_import_menu()
    import_uoms_page.go_to_import_uom()

    # UPLOAD FILE BENAR
    import_uoms_page.upload_xls("data/master_uoms.xls")
    import_uoms_page.submit()

    # VALIDASI ALERT
    WebDriverWait(driver, 10).until(
        EC.url_contains("/master/uoms")
    )

    assert "/master/uoms" in driver.current_url