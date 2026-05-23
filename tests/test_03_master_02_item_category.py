import os
import pytest

from pages.login_page import LoginPage
from pages.item_categories_page import ItemCategoryPage
from utils.helper import clear_and_fill, set_select_value





def test_create_item_category_success(driver):
    login_page = LoginPage(driver)
    item_categories_page = ItemCategoryPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # login
    login_page.open(base_url)
    login_page.login(email, password)

    # ke Item Categories page
    item_categories_page.go_to_item_categories()

    # create Item Cateogory
    item_categories_page.click_create()
    code = item_categories_page.fill_form_random(1)
    item_categories_page.submit()