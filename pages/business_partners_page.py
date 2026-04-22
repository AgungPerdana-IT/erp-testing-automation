from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import uuid

from utils.helper import input_text, select_random, select_checkbox
from utils.generator import *

class BusinessPartnersPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_business_partners(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Master']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/master/partners']"))).click()

    def click_create(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='/master/partners/create']")
        )).click()

        self.wait.until(EC.visibility_of_element_located((By.NAME, "code")))

    def fill_form_random(self, index):
        code = f"BP-{index:03d}-{uuid.uuid4().hex[:4]}"

        input_text(self.driver, self.wait, By.NAME, "code", code)
        input_text(self.driver, self.wait, By.NAME, "name", random_company())
        
        select_checkbox(self.driver, self.wait)

        select_random(self.driver, self.wait, "is_active", exclude_zero=False)
        
        input_text(self.driver, self.wait, By.NAME, "tax_id", random_npwp())
        input_text(self.driver, self.wait, By.NAME, "email", random_email())
        input_text(self.driver, self.wait, By.NAME, "phone", random_phone())

        select_random(self.driver, self.wait, "currency_code")
        
        input_text(self.driver, self.wait, By.NAME, "payment_terms_days", str(random.randint(0, 360)))
        input_text(self.driver, self.wait, By.NAME, "address", random_address())
        input_text(self.driver, self.wait, By.NAME, "city", random_city())
        input_text(self.driver, self.wait, By.NAME, "country", random_country())
        input_text(self.driver, self.wait, By.NAME, "postal_code", random_postal_code())
        input_text(self.driver, self.wait, By.NAME, "notes", random_note())

        return code

    def submit(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and normalize-space()='Create']")
        )).click()

        self.wait.until(EC.url_contains("/master/partners"))