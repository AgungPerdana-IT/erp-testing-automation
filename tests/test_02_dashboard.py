import os
import pytest
from dotenv import load_dotenv

from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.helper import clear_and_fill, set_select_value


load_dotenv()


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_click_dashboard_success(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # login
    login_page.open(base_url)
    login_page.login(email, password)

    # ke dasboard page
    dashboard_page.go_to_dashboard()


# def test_click_logo_success(driver):
#     login_page = LoginPage(driver)
#     dashboard_page = DashboardPage(driver)

#     base_url = os.getenv("BASE_URL")
#     email = os.getenv("TEST_EMAIL")
#     password = os.getenv("TEST_PASSWORD")

#     # login
#     login_page.open(base_url)
#     login_page.login(email, password)

#     # ke dasboard page
#     dashboard_page.go_to_dashboard()