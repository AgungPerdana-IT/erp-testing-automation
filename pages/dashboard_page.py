from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import uuid

from utils.helper import input_text, select_random
from utils.generator import random_name, random_note


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_dashboard(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Dashboard']"))).click()

# class DashboardPage:

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)

#     def go_to_dashboard(self):
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Dashboard']"))).click()