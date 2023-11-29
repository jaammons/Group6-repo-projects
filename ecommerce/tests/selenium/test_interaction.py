from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
from time import sleep
from validation import *
from utilities import *
from reports import *    

@pytest.fixture(scope="session")
def initialize_driver():
    """
    Returns an initialized ChromeDriver.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def driver(initialize_driver):
    initialize_driver.get("http://127.0.0.1:8000/")
    yield initialize_driver
    initialize_driver.get("http://127.0.0.1:8000/users/logout")
   

@pytest.fixture
def admin_driver(driver):
    """
    Returns a ChromeDriver logged in as Admin on homepage.
    """
    yield login(driver)

def login(driver):
    driver.get("http://127.0.0.1:8000/users/login")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("Admin")
    driver.find_element(By.NAME, "login").click()
    return driver

class TestSelenium:

    def test_login(self, admin_driver, test_log):
        """
        Test verifies admin_login was successful by checking user greeting
        on index.html after log in attempt.
        Expected result: Admin is logged in.
        """
        try:
            expected = "Welcome, Admin."
            greeting = admin_driver.find_element(By.ID, "greeting")
            assert greeting.text == expected
            log_result("Login Functionality", "Pass", test_log)
        except NoSuchElementException:
            log_result("Login Functionality", "Welcome greeting missing.", test_log)
        except AssertionError:
            log_result("Login Functionality", f"Incorrect value for greeting. Expected {expected}, got {greeting.text}", test_log)

    def test_logout(self, admin_driver, test_log):
        """
        Test verifies log out was successful by checking user greeting
        on index.html after log out attempt.
        Expected result: User is logged out.
        """
        try:
            expected = "Not signed in."
            admin_driver.find_element(By.ID, "logout").click()
            greeting = admin_driver.find_element(By.ID, "greeting")
            assert greeting.text == expected
            log_result("Logout Functionality", "Pass", test_log)
        except NoSuchElementException:
            log_result("Logout Functionality", "Not signed in message missing.", test_log)
        except AssertionError:
            log_result("Logout Functionality", f"Incorrect value for logged out message. Expected {expected}, got {greeting.text}", test_log)

    def test_url_titles(self, driver, test_log):
        """
        This test verifies the ability to load all the website pages and confirms their titles are correct.
        Expected result: All pages exist and titles match key values.
        """
        # List of pages to check
        url_titles = [{"users/login":"Log In"}, {"users/register":"Registration"}, {"index":"Auctions"}, {"watchlist":"Watchlist"}, {"add_listing":"Add Listing"},
                {"category/shoes":"Shoes"}]
        
        # Check pages that don't require log in / require being logged out
        for item in url_titles[:2]:
            url, title = item.popitem()
            driver.get("http://127.0.0.1:8000/" + url)
            try:
                assert title in driver.title
            except AssertionError:
                log_result(f"URL Titles: {title}", f"Fail, Expected {title}, got {driver.title}", test_log)

        # Check pages that require log in
        driver = login(driver)
        for item in url_titles[2:]:
            url, title = item.popitem()
            driver.get("http://127.0.0.1:8000/" + url)
            try:
                assert title in driver.title 
            except AssertionError:
                log_result(f"URL Titles: {title}", f"Fail, Expected {title}, got {driver.title}", test_log)
        log_result(f"URL Titles: ", "Pass", test_log)
        
    def test_listings(self, driver, test_log):
        """
        Test verifies that the homepage is showing active listings by searching for
        the listing container class name in the django template.
        Expected result: item-container class exists.
        """
        try:
            assert element_exists(driver, By.CLASS_NAME, "item-container")
        except NoSuchElementException:
            log_result("Test Listings", "Active listings missing from index.", test_log)
        log_result("Listings display on page", "Pass", test_log)