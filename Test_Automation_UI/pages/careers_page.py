from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CareersPage:
    is_careers_page_locator = (By.CSS_SELECTOR, "router.career-page")
    locations_block_locator = (By.CSS_SELECTOR, "#career-our-location")
    teams_block_locator = (By.CSS_SELECTOR, "#career-find-our-calling")
    life_at_insider_block_locator = (By.CSS_SELECTOR, ".elementor-element-a8e7b90")
    go_to_qa_jobs_page_locator = (By.LINK_TEXT, "Find your dream job")

    def __init__(self, driver):
        self.driver = driver

    def is_careers_page_opened(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.is_careers_page_locator)
        )

    def are_blocks_present(self):
        locations_block = self.driver.find_element(*self.locations_block_locator)
        teams_block = self.driver.find_element(*self.teams_block_locator)
        life_at_insider_block = self.driver.find_element(*self.life_at_insider_block_locator)

        return all([locations_block, teams_block, life_at_insider_block])

    def go_to_qa_jobs_page(self):
        self.driver.find_element(*self.go_to_qa_jobs_page_locator).click()
        return WebDriverWait(self.driver, 10).until(
            EC.url_contains("https://useinsider.com/careers/open-positions/")
        )

