from datetime import date
from random import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

from utils.helper import *
from utils.generator import *


class ReconciliationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =============================
    # NAVIGATION
    # =============================
    def go_to_reconciliation(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Cash & Bank']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/cash-bank/reconcile']"))).click()


    # =============================
    # ACTION
    # =============================
    
    def fill_form_random(self, index):
        select_random(self.driver, self.wait, "account_id")

    def filter(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and normalize-space()='Filter']")
        )).click()

    def upload_xls(self, file_name):
        file_path = os.path.abspath(file_name)

        file_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "csv"))
        )

        file_input.send_keys(file_path)

    def preview(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.btn-primary")
        )).click()


    def submit(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.btn-primary")
        )).click()
