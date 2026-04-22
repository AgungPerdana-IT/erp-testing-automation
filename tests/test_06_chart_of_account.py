import os
import pytest
from dotenv import load_dotenv

from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.chart_of_accounts_page import ChartOfAccountPage
from utils.helper import clear_and_fill, set_select_value


load_dotenv()


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_create_chart_of_account_success(driver):
    login_page = LoginPage(driver)
    chart_of_accounts_page = ChartOfAccountPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # login
    login_page.open(base_url)
    login_page.login(email, password)

    # ke Chart Of Accounts page
    chart_of_accounts_page.go_to_chart_of_account()

    # create Chart Of Account
    chart_of_accounts_page.click_create()
    code = chart_of_accounts_page.fill_form_random(1)
    chart_of_accounts_page.submit()