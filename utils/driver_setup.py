from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

def get_driver():
    options = Options()
    options.binary_location = "/snap/bin/chromium"
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager(
                chrome_type=ChromeType.CHROMIUM,
                driver_version="147.0.7727.116"
            ).install()
        ),
        options=options
    )

    return driver