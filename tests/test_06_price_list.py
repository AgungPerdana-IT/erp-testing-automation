import os
import pytest
from dotenv import load_dotenv

from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.price_lists_page import PriceListsPage
from utils.helper import clear_and_fill, set_select_value


load_dotenv()


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_create_price_list_success(driver):
    login_page = LoginPage(driver)
    price_lists_page = PriceListsPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # login
    login_page.open(base_url)
    login_page.login(email, password)

    # ke Price Lists page
    price_lists_page.go_to_price_lists()

    # create Price List
    price_lists_page.click_create()
    code = price_lists_page.fill_form_random(1)
    price_lists_page.submit()