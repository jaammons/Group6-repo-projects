from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import pytest
from time import sleep
from utilities import *   

def login(driver: webdriver.Chrome, username: str, password: str) -> webdriver.Chrome:
    """
    Navigates chromedriver to login page and submits login form with given arguments.
    """
    driver.get("http://127.0.0.1:8000/users/login")
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "login").click()
    return driver

class TestSelenium():
    def test_login(self, user_driver: webdriver.Chrome, log: dict) -> None:
        """
        Verifies log in functionality by attempting to log in a user and checking greeting on index after log in attempt. 
        Expected result: User is logged in.
        """
        try:
            # Check expected greeting on index
            expected = "Welcome, User."  # Output is Welcome, <username>, but the test user is User.
            greeting = user_driver.find_element(By.ID, "greeting").text
            assert greeting == expected
            log_result("pass", log)

        except (NoSuchElementException, AssertionError) as e:
            # log errors and capture screenshot
            log_result("fail", log, f"{type(e).__name__} : {str(e)}" if type(e) == AssertionError else f"{type(e).__name__} : {e.msg}")
            capture_screenshot(user_driver, "test_login_actual")

    def test_logout(self, user_driver, log) -> None:
        """
        Verifies log out was successful by checking user greeting on index after log out attempt.
        Expected result: User is logged out.
        """
        try:
            # Check expected greeting on index
            expected = "Not signed in."
            user_driver.find_element(By.ID, "logout").click()
            greeting = user_driver.find_element(By.ID, "greeting")
            assert greeting.text == expected
            log_result("pass", log)

        except (NoSuchElementException, AssertionError) as e:
            # log errors and capture screenshot
            log_result("fail", log, f"{type(e).__name__} : {str(e)}" if type(e) == AssertionError else f"{type(e).__name__} : {e.msg}")
            capture_screenshot(user_driver, "test_logout_actual")

    def test_url_titles(self, driver: webdriver.Chrome, log: dict) -> None:
        """
        Verifies the ability to load all the website pages and confirms their titles are correct.
        Expected result: All pages exist and titles match key values.
        """
        # List of pages to check
        url_titles = [{"users/register":"Registration"}, {"users/login":"Log In"}, {"index":"Auctions"}, {"watchlist":"Watchlist"}, {"add_listing":"Add Listing"},
                {"category/shoes":"Shoes"}]
        
        try:
            for index, item in enumerate(url_titles):  
                # log in after viewing registration and log in pages
                if index == 2:
                    driver = login(driver, "User", "testuser1")

                # Compare expected and actual titles
                url, title = item.popitem()
                driver.get("http://127.0.0.1:8000/" + url)
                assert title in driver.title
            log_result("pass", log)

        except AssertionError as e:
            # log errors and capture screenshot
            log_result("fail", log, f"{type(e).__name__} : {str(e)}")
            capture_screenshot(driver, f"test_url_titles_actual")
        
    def test_listings(self, driver: webdriver.Chrome, log: dict) -> None:
        """
        Verifies that the homepage is showing active listings by searching for the listing container class name in the django template.
        Expected result: item-container class exists.
        """
        try:
            assert len(driver.find_elements(By.CLASS_NAME, "item-container")) > 0
            log_result("pass", log)
        except NoSuchElementException as e:
            # log errors and capture screenshot
            log_result("fail", log, f"{type(e).__name__} : {e.msg}")
            capture_screenshot(driver, "test_listings_actual")
        

    def test_category_dropdown(self, user_driver: webdriver.Chrome, log: dict) -> None:
        """
        Verifies category dropdown selection from active listings page redirects user to the appropriate category.
        Expected outcome: User redirected to selected category page.
        """
        try:
            # Check if category dropdown exists
            category_dropdown = user_driver.find_element(By.NAME, "category")

            # Select a category and submit choice
            Select(category_dropdown).select_by_visible_text("Watches")
            user_driver.find_element(By.ID, "category_select").click()

            # Verify page loads with right category
            auctions = user_driver.find_elements(By.CLASS_NAME, "item-name")
            assert len(auctions) == 4

            items = ["Fossil Watch", "Golden Hour Watch", "Casio Watch", "Timex Watch"]
            for auction in auctions:
                assert auction.text in items
            log_result("pass", log)

        except (NoSuchElementException, AssertionError) as e:
            # log errors and capture screenshot
            log_result("fail", log, f"{type(e).__name__} : {str(e)}" if type(e) == AssertionError else f"{type(e).__name__} : {e.msg}")
            capture_screenshot(user_driver, "test_category_dropdown_actual")

    def test_validate_registration_form_fields(self, driver: webdriver.Chrome, log: dict) -> None:
        """
        Verifies all form fields are present on registration form.
        Expected result: All fields are present.
        """
        driver.get("http://127.0.0.1:8000/users/register")

        try:
            # Verify elements exist, selenium will throw NoSuchElementException for any missing element
            driver.find_element(By.NAME, "username")
            driver.find_element(By.NAME, "email")
            driver.find_element(By.NAME, "password")
            driver.find_element(By.NAME, "confirmation")
            driver.find_element(By.NAME, "register")
            log_result("pass", log)

        except NoSuchElementException as e:
            # log errors and capture screenshot
            log_result("fail", log, f"{type(e).__name__} : {e.msg}")
            capture_screenshot(driver, "test_validate_registration_form_fields_actual")
            
    def test_registration(self, driver: webdriver.Chrome, log: dict) -> None:
        """
        Verifies user registration by attempting to register a new user and checking the user greeting after login.
        """
        driver.get("http://127.0.0.1:8000/users/register")
        try:
            # Enter registration info
            driver.find_element(By.NAME, "username").send_keys("RegistrationTest")
            driver.find_element(By.NAME, "email").send_keys("Testuser@gmail.com")
            driver.find_element(By.NAME, "password").send_keys("Register123")
            driver.find_element(By.NAME, "confirmation").send_keys("Register123")
            driver.find_element(By.NAME, "register").click()

            # Check expected greeting on index
            expected = "Welcome, RegistrationTest."  # Output is Welcome, <username>, but the test user is User.
            greeting = driver.find_element(By.ID, "greeting").text
            assert greeting == expected
            log_result("pass", log)

        except (NoSuchElementException, AssertionError) as e:
            # log errors and capture screenshot
            log_result("fail", log, f"{type(e).__name__} : {str(e)}" if type(e) == AssertionError else f"{type(e).__name__} : {e.msg}")
            capture_screenshot(driver, "test_registration_actual")

        # Send server request to delete test user
        driver.get("http://127.0.0.1:8000/users/delete_user?username=RegistrationTest")