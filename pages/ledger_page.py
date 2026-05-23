from datetime import date
from random import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

from utils.helper import *
from utils.generator import *


class LedgerPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_ledger(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Cash & Bank']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/cash-bank/ledger']"))).click()


        self.wait.until(EC.url_contains("/cash-bank/ledger"))