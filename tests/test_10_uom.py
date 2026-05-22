import os
import pytest

from pages.login_page import LoginPage
from pages.uoms_page import UomPage
from utils.helper import clear_and_fill, set_select_value



def test_create_UoM_success(driver):
    login_page = LoginPage(driver)
    uoms_page = UomPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # login
    login_page.open(base_url)
    login_page.login(email, password)

    # ke Uoms page
    uoms_page.go_to_uoms()

    # create Uom
    uoms_page.click_create()
    code = uoms_page.fill_form_random(1)
    uoms_page.submit()