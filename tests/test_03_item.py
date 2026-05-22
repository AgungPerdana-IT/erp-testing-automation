import os
import pytest

from pages.login_page import LoginPage
from pages.items_page import ItemPage
from utils.helper import clear_and_fill, set_select_value




def test_create_item_success(driver):
    login_page = LoginPage(driver)
    items_page = ItemPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # login
    login_page.open(base_url)
    login_page.login(email, password)

    # ke Items page
    items_page.go_to_items()

    # create Item
    items_page.click_create()
    code = items_page.fill_form_random(1)
    items_page.submit()