import pytest
import time
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QaJobsPage
from utils.browser_factory import BrowserFactory


@pytest.mark.parametrize("browser", ["chrome"])
def test_insider_qa_job_search(browser):
    driver = None
    try:
        # Initialize browser
        driver = BrowserFactory(browser).get_driver()
        driver.maximize_window()

        # Step 1: Visit Insider home page and check if opened
        home_page = HomePage(driver)
        home_page.go_to_home_page()
        assert home_page.is_home_page_opened(), "Home page not opened!"

        # Step 2: Navigate to Careers page and check blocks
        home_page.go_to_careers_page()
        careers_page = CareersPage(driver)
        assert careers_page.is_careers_page_opened(), "Careers page not opened!"
        assert careers_page.are_blocks_present(), "Some blocks on Careers page are missing!"

        # Step 3: Go to QA jobs page, filter by Istanbul and Quality Assurance
        careers_page.go_to_qa_jobs_page()
        qa_jobs_page = QaJobsPage(driver)
        qa_jobs_page.filter_jobs(location="Istanbul, Turkey", department="Quality Assurance")
        assert qa_jobs_page.are_jobs_filtered_correctly(location="Istanbul, Turkey", department="Quality Assurance"), \
            "Jobs are not filtered correctly!"

        # Step 4: Check redirection to Lever application form
        assert qa_jobs_page.click_view_role_and_verify_redirect(), "Redirect to Lever Application form failed!"

    except AssertionError as e:
        # Take screenshot if test fails
        driver.save_screenshot(f"screenshots/test_fail_{time.strftime('%Y%m%d_%H%M%S')}.png")
        raise e

    finally:
        if driver:
            driver.quit()
