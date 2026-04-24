from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class ImportItemsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =============================
    # NAVIGATION
    # =============================
    def go_to_import_menu(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Master']")
        )).click()

        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='/master/import']")
        )).click()

    def go_to_import_item(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='/master/import/items']")
        )).click()

        self.wait.until(EC.visibility_of_element_located((By.NAME, "csv")))

    # =============================
    # ACTION
    # =============================
    def upload_csv(self, file_name):
        file_path = os.path.abspath(file_name)

        file_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "csv"))
        )

        file_input.send_keys(file_path)

    def submit(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Upload & Import']")
        )).click()

        # self.wait.until(EC.url_contains("/master/items"))