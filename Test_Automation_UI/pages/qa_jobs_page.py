import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class QaJobsPage:
    location_filter_locator = (By.CSS_SELECTOR, "#select2-filter-by-location-container")
    select_element_locator = (By.ID, 'filter-by-location')
    department_filter_locator = (By.CSS_SELECTOR, "#select2-filter-by-department-container")
    select_element_department_locator = (By.ID, 'filter-by-department')
    job_cards_locator =(By.CSS_SELECTOR, ".position-list-item")
    career_position_list_locator =(By.CSS_SELECTOR, '#career-position-list .row')
    position_locator = (By.CSS_SELECTOR, ".position-title")
    department_name_locator = (By.CSS_SELECTOR, ".position-department")
    job_location_locator = (By.CSS_SELECTOR, ".position-location")
    element_action_locator = (By.CSS_SELECTOR, ".position-list-item")
    view_role_button_locator = (By.LINK_TEXT, "View Role")


    def __init__(self, driver):
        self.driver = driver

    def filter_jobs(self, location, department):
        # location
        location_filter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.location_filter_locator)
        )
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", location_filter)
        time.sleep(1)
        location_filter.click()
        time.sleep(1)
        select_element = self.driver.find_element(*self.select_element_locator)
        select = Select(select_element)
        for option in select.options:
            if option.text == location:
                self.driver.execute_script("arguments[0].scrollIntoView();", option)
                option.click()
        time.sleep(2)

        # department
        department_filter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.department_filter_locator)
        )
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", department_filter)
        time.sleep(1)
        department_filter.click()
        time.sleep(1)
        select_element = self.driver.find_element(*self.select_element_department_locator)
        select = Select(select_element)
        for option in select.options:
            if option.text == department:
                self.driver.execute_script("arguments[0].scrollIntoView();", option)
                option.click()
        time.sleep(1)
        department_filter.click()
        time.sleep(1)

    def are_jobs_filtered_correctly(self, location, department):
        job_cards = self.driver.find_elements(*self.job_cards_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",
                                   self.driver.find_element(*self.career_position_list_locator))
        time.sleep(1)
        for job in job_cards:
            position = job.find_element(*self.position_locator).text
            department_name = job.find_element(*self.department_name_locator).text
            job_location = job.find_element(*self.job_location_locator).text

            if "Quality Assurance" not in position or department_name != department or location not in job_location:
                return False
        return True

    def click_view_role_and_verify_redirect(self):
        element = self.driver.find_element(*self.element_action_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)
        view_role_button = self.driver.find_element(*self.view_role_button_locator)
        view_role_button.click()

        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
        return WebDriverWait(self.driver, 10).until(
            EC.url_contains("lever.co")
        )
