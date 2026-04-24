import os
import pytest
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.import_bussines_partners_page import ImportBussinesPartnersPage

load_dotenv()


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


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

    # UPLOAD CSV SALAH
    import_bussines_partners_page.upload_csv("data/master_wrong_header.csv")
    import_bussines_partners_page.submit()

    # VALIDASI ALERT
    alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger"))
    )

    # DEBUG (boleh ada, tapi optional)
    print("Alert text:", alert.text)

    # ASSERT (INI YANG PENTING)
    assert "Required CSV header" in alert.text


def test_import_business_partner_succses(driver):
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

    # UPLOAD CSV SALAH
    import_bussines_partners_page.upload_csv("data/master_partners.csv")
    import_bussines_partners_page.submit()

    # VALIDASI ALERT
    WebDriverWait(driver, 10).until(
        EC.url_contains("/master/partners")
    )

    assert "/master/partners" in driver.current_url