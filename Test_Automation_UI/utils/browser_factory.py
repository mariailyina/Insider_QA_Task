import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class BrowserFactory:
    def __init__(self, browser):
        self.browser = browser.lower()

    def get_driver(self):
        if self.browser == 'chrome':
            return webdriver.Chrome()
        else:
            raise ValueError(f"Browser '{self.browser}' is not supported")
