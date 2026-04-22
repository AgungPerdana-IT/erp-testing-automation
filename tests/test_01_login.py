import os
import pytest
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_setup import get_driver
from pages.login_page import LoginPage


# =============================
# Load environment variable
# =============================
load_dotenv()


# =============================
# Pytest fixture (setup & teardown)
# =============================
@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


# =============================
# Test Case: Login Success
# =============================
def test_login_success(driver):
    login_page = LoginPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # buka halaman login
    login_page.open(base_url)

    # login
    login_page.login(email, password)

    # validasi: URL berubah ke dashboard
    WebDriverWait(driver, 10).until(
        EC.url_contains("dashboard")
    )

    assert "dashboard" in driver.current_url


# =============================
# Test Case: Login Wrong Password
# =============================
def test_login_wrong_password(driver):
    login_page = LoginPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = "123456"  # intentionally wrong password

    login_page.open(base_url)

    # isi email + password
    login_page.input_email(email)
    login_page.input_password(password)

    # disable browser validation
    login_page.disable_browser_validation()

    # klik login
    login_page.click_login()



# =============================
# Test Case: Login wrong Email
# =============================
def test_login_wrong_email(driver):
    login_page = LoginPage(driver)

    base_url = os.getenv("BASE_URL")
    email = "salah@mail.com"  # intentionally wrong email
    password = os.getenv("TEST_PASSWORD")

    login_page.open(base_url)

    # isi email + password
    login_page.input_email(email)
    login_page.input_password(password)

    # disable browser validation
    login_page.disable_browser_validation()

    # klik login
    login_page.click_login()


# =============================
# Test Case: Login Email Kosong
# =============================
def test_login_empty_email(driver):
    login_page = LoginPage(driver)

    base_url = os.getenv("BASE_URL")
    password = os.getenv("TEST_PASSWORD")

    login_page.open(base_url)

    # isi hanya password
    login_page.input_password(password)

    # disable browser validation
    login_page.disable_browser_validation()

    # klik login
    login_page.click_login()

# =============================
# Test Case: Login Password Kosong
# =============================
def test_login_empty_password(driver):
    login_page = LoginPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")

    login_page.open(base_url)

    # isi hanya email
    login_page.input_email(email)

    # disable browser validation
    login_page.disable_browser_validation()

    # klik login
    login_page.click_login()


# =============================
# Test Case: Login Credential Salah
# =============================
def test_login_wrong_credentials(driver):
    login_page = LoginPage(driver)

    base_url = os.getenv("BASE_URL")

    login_page.open(base_url)
    login_page.login("salah@email.com", "123456")

    # disable browser validation
    login_page.disable_browser_validation()

    # klik login
    login_page.click_login()


# =============================
# Test Case: Login Email dan Password kosong
# =============================


def test_login_empty_password(driver):
    login_page = LoginPage(driver)

    base_url = os.getenv("BASE_URL")

    login_page.open(base_url)

    # disable browser validation
    login_page.disable_browser_validation()

    # klik login
    login_page.click_login()