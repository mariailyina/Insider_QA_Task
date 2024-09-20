import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class QaJobsPage:
    def __init__(self, driver):
        self.driver = driver

    def filter_jobs(self, location, department):
        # location
        location_filter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#select2-filter-by-location-container"))
        )
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", location_filter)
        time.sleep(1)
        location_filter.click()
        time.sleep(1)
        select_element = self.driver.find_element(By.ID, 'filter-by-location')
        select = Select(select_element)
        for option in select.options:
            if option.text == location:
                self.driver.execute_script("arguments[0].scrollIntoView();", option)
                option.click()
        time.sleep(2)

        # department
        department_filter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#select2-filter-by-department-container"))
        )
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", department_filter)
        time.sleep(1)
        department_filter.click()
        time.sleep(1)
        select_element = self.driver.find_element(By.ID, 'filter-by-department')
        select = Select(select_element)
        for option in select.options:
            if option.text == department:
                self.driver.execute_script("arguments[0].scrollIntoView();", option)
                option.click()
        time.sleep(1)
        department_filter.click()
        time.sleep(1)

    def are_jobs_filtered_correctly(self, location, department):
        job_cards = self.driver.find_elements(By.CSS_SELECTOR, ".position-list-item")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",
                                   self.driver.find_element(By.CSS_SELECTOR, '#career-position-list .row'))
        time.sleep(1)
        for job in job_cards:
            position = job.find_element(By.CSS_SELECTOR, ".position-title").text
            department_name = job.find_element(By.CSS_SELECTOR, ".position-department").text
            job_location = job.find_element(By.CSS_SELECTOR, ".position-location").text

            if "Quality Assurance" not in position or department_name != department or location not in job_location:
                return False
        return True

    def click_view_role_and_verify_redirect(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".position-list-item")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)
        view_role_button = self.driver.find_element(By.LINK_TEXT, "View Role")
        view_role_button.click()

        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
        return WebDriverWait(self.driver, 10).until(
            EC.url_contains("lever.co")
        )
