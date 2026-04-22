from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import uuid

from utils.helper import input_text, select_random
from utils.generator import random_item, random_note


class ItemPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_items(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Master']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/master/items']"))).click()

    def click_create(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='/master/items/create']")
        )).click()

        self.wait.until(EC.visibility_of_element_located((By.NAME, "code")))

    def fill_form_random(self, index):
        code = f"item-{index:03d}-{uuid.uuid4().hex[:4]}"
        sku = f"SKU-{index:04d}-{uuid.uuid4().hex[:4]}"

        input_text(self.driver, self.wait, By.NAME, "code", code)
        input_text(self.driver, self.wait, By.NAME, "sku", sku)
        input_text(self.driver, self.wait, By.NAME, "name", random_item())

        select_random(self.driver, self.wait, "item_type", exclude_zero=False)
        select_random(self.driver, self.wait, "category_id")
        select_random(self.driver, self.wait, "uom_id")
        select_random(self.driver, self.wait, "currency_code")

        input_text(self.driver, self.wait, By.NAME, "barcode", str(random.randint(10000000, 99999999)))
        input_text(self.driver, self.wait, By.NAME, "default_purchase_price", str(random.randint(1000, 100000)))
        input_text(self.driver, self.wait, By.NAME, "default_sales_price", str(random.randint(1000, 100000)))
        input_text(self.driver, self.wait, By.NAME, "weight_kg", str(random.randint(1, 100)))

        select_random(self.driver, self.wait, "is_active", exclude_zero=False)
        input_text(self.driver, self.wait, By.NAME, "notes", random_note())

        return code

    def submit(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and normalize-space()='Create']")
        )).click()

        self.wait.until(EC.url_contains("/master/items"))