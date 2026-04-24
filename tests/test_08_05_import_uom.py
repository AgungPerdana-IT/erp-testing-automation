import os
import pytest
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.import_uoms_page import ImportUomsPage

load_dotenv()


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


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

    # UPLOAD CSV SALAH
    import_uoms_page.upload_csv("data/master_wrong_header.csv")
    import_uoms_page.submit()

    # VALIDASI ALERT
    alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger"))
    )

    # ASSERT (INI YANG PENTING)
    assert "Required CSV header" in alert.text


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

    # UPLOAD CSV SALAH
    import_uoms_page.upload_csv("data/master_uoms.csv")
    import_uoms_page.submit()

    # VALIDASI ALERT
    WebDriverWait(driver, 10).until(
        EC.url_contains("/master/uoms")
    )

    assert "/finance/chart-of-account" in driver.current_url