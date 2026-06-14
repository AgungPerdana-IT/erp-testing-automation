from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import uuid

from utils.helper import *
from utils.generator import *


class OverviewPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_reports(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Reports']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/reports']"))).click()

    def go_to_overview(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/reports/balance-sheet']"))).click()
        print("Current URL:", self.driver.current_url)

        elements = self.driver.find_elements(
            By.CSS_SELECTOR,
            "a[href='/reports/balance-sheet']"
        )

        print("Found:", len(elements))
        self.wait.until(EC.url_contains("/reports/balance-sheet"))