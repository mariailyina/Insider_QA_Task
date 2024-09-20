import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://useinsider.com/"

    def go_to_home_page(self):
        self.driver.get(self.url)
        time.sleep(1)
        try:
            self.driver.find_element(By.CSS_SELECTOR, '#wt-cli-accept-all-btn').click()
        except:
            None

    def is_home_page_opened(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "router.home-page"))
        )

    def go_to_careers_page(self):
        company_menu = self.driver.find_element(By.LINK_TEXT, "Company")
        company_menu.click()
        careers_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Careers"))
        )
        careers_menu.click()
