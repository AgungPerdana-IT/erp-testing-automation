import os
import pytest
from dotenv import load_dotenv

from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.warehouses_page import WarehousesPage
from utils.helper import clear_and_fill, set_select_value


load_dotenv()


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_create_warehouse_success(driver):
    login_page = LoginPage(driver)
    warehouses_page = WarehousesPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # login
    login_page.open(base_url)
    login_page.login(email, password)

    # ke Warehouses page
    warehouses_page.go_to_warehouses()

    # create Warehouse
    warehouses_page.click_create()
    code = warehouses_page.fill_form_random(1)
    warehouses_page.submit()