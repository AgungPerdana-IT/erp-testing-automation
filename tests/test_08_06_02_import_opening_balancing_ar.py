import os
import pytest
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.import_opening_balancing_ar_page import ImportBalancingARPage

load_dotenv()


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_import_balancing_ar_wrong_header(driver):
    login_page = LoginPage(driver)
    import_balancing_ar_page = ImportBalancingARPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_balancing_ar_page.go_to_import_menu()
    import_balancing_ar_page.go_to_import_balancing_ar()

    # PILIH TANGGAL
    import_balancing_ar_page.set_txn_date_today()

    # UPLOAD FILE SALAH
    import_balancing_ar_page.upload_xls("data/master_wrong_header.xls")
    import_balancing_ar_page.submit()

    # VALIDASI ALERT
    alert_message = import_balancing_ar_page.get_error_alert_message()
    assert "Kolom header harus ada: account_code, debit, credit (+ memo optional)" in alert_message


def test_import_balancing_ar_success(driver):
    login_page = LoginPage(driver)
    import_balancing_ar_page = ImportBalancingARPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # LOGIN
    login_page.open(base_url)
    login_page.login(email, password)

    # NAVIGASI
    import_balancing_ar_page.go_to_import_menu()
    import_balancing_ar_page.go_to_import_balancing_ar()

    # PILIH TANGGAL
    import_balancing_ar_page.set_txn_date_today()

    # UPLOAD CSV SALAH
    import_balancing_ar_page.upload_xls("data/opening_ar.xls")
    import_balancing_ar_page.submit()

    # VALIDASI ALERT
    WebDriverWait(driver, 10).until(
        EC.url_contains("/finance/ar-invoices")
    )

    assert "/finance/ar-invoices" in driver.current_url