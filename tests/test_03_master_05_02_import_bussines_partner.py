import os
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.import_bussines_partners_page import ImportBussinesPartnersPage



def test_import_business_partner_wrong_header(driver):
    login_page = LoginPage(driver)
    import_bussines_partners_page = ImportBussinesPartnersPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_bussines_partners_page.go_to_import_menu()
    import_bussines_partners_page.go_to_import_business_partner()

    # UPLOAD FILE SALAH
    import_bussines_partners_page.upload_xls("data/master_wrong_header.xls")
    import_bussines_partners_page.submit()

    # VALIDASI ALERT
    alert_message = import_bussines_partners_page.get_error_alert_message()
    assert "Kolom header harus ada: code, name, is_customer, is_supplier, currency_code, is_active" in alert_message


def test_import_business_partner_success(driver):
    login_page = LoginPage(driver)
    import_bussines_partners_page = ImportBussinesPartnersPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_bussines_partners_page.go_to_import_menu()
    import_bussines_partners_page.go_to_import_business_partner()

    # UPLOAD FILE BENAR
    import_bussines_partners_page.upload_xls("data/master_partners.xls")
    import_bussines_partners_page.submit()

    # VALIDASI ALERT
    WebDriverWait(driver, 10).until(
        EC.url_contains("/master/partners")
    )

    assert "/master/partners" in driver.current_url 