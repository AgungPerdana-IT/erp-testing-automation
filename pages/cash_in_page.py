from datetime import date
from random import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

from utils.helper import *
from utils.generator import *


class CashInPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_cash_in(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Cash & Bank']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/cash-bank/cash-in']"))).click()

    def click_create(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='/cash-bank/cash-in/create']")
        )).click()

        self.wait.until(EC.visibility_of_element_located((By.NAME, "txn_date")))

    # =============================
    # ACTION
    # =============================
    def set_txn_date_today(self):
        today = date.today().strftime("%Y-%m-%d")
        txn_date_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "txn_date"))
        )
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", txn_date_input, today
        )
    
    def fill_form_random(self, index):
        select_random(self.driver, self.wait, "account_id", exclude_zero=False)
        input_text(self.driver, self.wait, By.NAME, "amount", str(round(random.uniform(0.0, 9.0), 2)))    
        select_random(self.driver, self.wait, "offset_account_code", exclude_zero=False)
        input_text(self.driver, self.wait, By.NAME, "description", random_note())




    def submit(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and normalize-space()='Post Cash In']")
        )).click()

        self.wait.until(EC.url_contains("/cash-bank/cash-in"))