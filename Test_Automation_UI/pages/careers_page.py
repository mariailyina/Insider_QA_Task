from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CareersPage:
    def __init__(self, driver):
        self.driver = driver

    def is_careers_page_opened(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "router.career-page"))
        )

    def are_blocks_present(self):
        locations_block = self.driver.find_element(By.CSS_SELECTOR, "#career-our-location")
        teams_block = self.driver.find_element(By.CSS_SELECTOR, "#career-find-our-calling")
        life_at_insider_block = self.driver.find_element(By.CSS_SELECTOR, ".elementor-element-a8e7b90")

        return all([locations_block, teams_block, life_at_insider_block])

    def go_to_qa_jobs_page(self):
        self.driver.find_element(By.LINK_TEXT, "Find your dream job").click()
