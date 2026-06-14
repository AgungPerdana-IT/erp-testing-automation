import os
from pages.import_chart_of_accounts_page import ImportChartOfAccountPage
import pytest

from pages.login_page import LoginPage
from pages.overview_page import OverviewPage

 

def test_go_to_balance_sheet(driver):
    login_page = LoginPage(driver)
    overview_page = OverviewPage(driver)

    base_url = os.getenv("BASE_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # login
    login_page.open(base_url)
    login_page.login(email, password)

    # ke reports page
    overview_page.go_to_reports()

    # VALIDASI PREVIEW
    assert "/reports" in driver.current_url

    # ke overview page
    overview_page.go_to_overview()

    # VALIDASI PREVIEW
    assert "/reports/balance-sheet" in driver.current_url
