import os
import pytest
from dotenv import load_dotenv

from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.payment_methods_page import PaymentMethodPage
from utils.helper import clear_and_fill, set_select_value


load_dotenv()


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_create_payment_method_success(driver):
    login_page = LoginPage(driver)
    payment_methods_page = PaymentMethodPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # login
    login_page.open(base_url)
    login_page.login(email, password)

    # ke Payment Methods page
    payment_methods_page.go_to_payment_methods()

    # create Payment Method
    payment_methods_page.click_create()
    code = payment_methods_page.fill_form_random(1)
    payment_methods_page.submit()