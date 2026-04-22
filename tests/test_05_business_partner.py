import os
import pytest
from dotenv import load_dotenv

from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.business_partners_page import BusinessPartnersPage
from utils.helper import clear_and_fill, set_select_value


load_dotenv()


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_create_business_partner_success(driver):
    login_page = LoginPage(driver)
    business_partners_page = BusinessPartnersPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # login
    login_page.open(base_url)
    login_page.login(email, password)

    # ke business partners page
    business_partners_page.go_to_business_partners()

    # create business partner
    business_partners_page.click_create()
    code = business_partners_page.fill_form_random(1)
    business_partners_page.submit()