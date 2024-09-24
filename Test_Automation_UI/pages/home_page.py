import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    accept_cookies_locator = (By.CSS_SELECTOR, '#wt-cli-accept-all-btn')
    is_home_page_locator = (By.CSS_SELECTOR, 'router.home-page')
    category_locator = (By.LINK_TEXT, "Company")
    sub_locator = (By.LINK_TEXT, "Careers")

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://useinsider.com/"

    def go_to_home_page(self):
        self.driver.get(self.url)
        time.sleep(1)
        try:
            self.driver.find_element(*self.accept_cookies_locator).click()
        except:
            None

    def is_home_page_opened(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.is_home_page_locator)
        )

    def go_to_careers_page(self):
        company_menu = self.driver.find_element(*self.category_locator)
        company_menu.click()
        careers_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sub_locator)
        )
        careers_menu.click()
        return WebDriverWait(self.driver, 10).until(
            EC.url_contains("https://useinsider.com/careers/")
        )
