from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, base_url):
        self.driver.get(f"{base_url}/login")

    def input_email(self, email):
        self.driver.find_element(By.ID, "lp-email").send_keys(email)

    def input_password(self, password):
        self.driver.find_element(By.ID, "lp-password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def login(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.click_login()

    def disable_browser_validation(self):
        self.driver.execute_script("""
            document.querySelector('form').noValidate = true;
        """)