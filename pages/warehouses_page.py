from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uuid

from utils.helper import *
from utils.generator import *

class WarehousesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_warehouses(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Master']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/master/warehouses']"))).click()

    def click_create(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='/master/warehouses/create']")
        )).click()

        self.wait.until(EC.visibility_of_element_located((By.NAME, "code")))

    def fill_form_random(self, index):
        code = f"WR-{index:03d}-{uuid.uuid4().hex[:4]}"

        input_text(self.driver, self.wait, By.NAME, "code", code)
        input_text(self.driver, self.wait, By.NAME, "name", random_company())
        
        select_random(self.driver, self.wait, "is_active", exclude_zero=False)
        
        input_text(self.driver, self.wait, By.NAME, "notes", random_note())

        return code

    def submit(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and normalize-space()='Create']")
        )).click()

        self.wait.until(EC.url_contains("/master/warehouses"))
        