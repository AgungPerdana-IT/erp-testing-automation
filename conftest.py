# conftest.py
import pytest
from dotenv import load_dotenv
from utils.driver_setup import get_driver

load_dotenv()  # ← cukup sekali di sini

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()