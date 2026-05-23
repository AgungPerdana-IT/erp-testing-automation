from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uuid
 
from utils.helper import *
from utils.generator import *

class AccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_accounts(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Cash & Bank']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/cash-bank/accounts']"))).click()

    def click_create(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='/cash-bank/accounts/create']")
        )).click()

        self.wait.until(EC.visibility_of_element_located((By.NAME, "code")))

    def fill_form_random(self, index):
        code = f"BANK-{index:03d}-{uuid.uuid4().hex[:4]}"
        input_text(self.driver, self.wait, By.NAME, "code", code)
        input_text(self.driver, self.wait, By.NAME, "name", random_bank())
        select_random(self.driver, self.wait, "type")
        select_random(self.driver, self.wait, "currency_code")
        select_random(self.driver, self.wait, "is_active", exclude_zero=False)
        select_random(self.driver, self.wait, "gl_account_id", exclude_zero=False)
        input_text(self.driver, self.wait, By.NAME, "bank_display_name", random_bank())
        input_text(self.driver, self.wait, By.NAME, "account_number", str(random.randint(10000000, 99999999)))
        input_text(self.driver, self.wait, By.NAME, "account_holder", random_company())

        return code

    def submit(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.btn-primary.erp-create-btn")
        )).click()

        self.wait.until(EC.url_contains("/cash-bank/accounts"))
        