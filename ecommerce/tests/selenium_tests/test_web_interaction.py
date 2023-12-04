from selenium import webdriver
from utilities import *
from time import sleep

import pytest

# Constants for login and registration form fields
LOGIN_USER_FORM_FIELDS = {"username": "User", "password": "testuser1"}
REGISTRATION_FORM_FIELDS = {"username": "RegistrationTest", "email": "Testuser@gmail.com", "password": "Register123", "confirmation": "Register123"}

def test_login(driver: webdriver.Chrome, live_server) -> None:
    """
    Tests the user login functionality.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        live_server: The live server fixture.

    Returns:
        None. Verifies the successful user login and the displayed greeting on the index page.
    """
    # Log in as User
    login(driver, live_server, LOGIN_USER_FORM_FIELDS)

    # Verify expected greeting on index
    expected = "Welcome, User."
    greeting = find_element(driver, "id", "greeting").text
    assert greeting == expected


def test_logout(driver: webdriver.Chrome, live_server) -> None:
    """
    Tests the user logout functionality.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        live_server: The live server fixture.

    Returns:
        None. Verifies the successful user logout and the displayed greeting indicating not being signed in on the index page.
    """
    # Log in as User
    login(driver, live_server, LOGIN_USER_FORM_FIELDS)

    # Click logout
    click(driver, "id", "logout")

    # Verify expected greeting
    expected_msg = "Not signed in."
    actual_msg = find_element(driver, "id", "greeting").text
    assert actual_msg == expected_msg


def test_url_titles(driver: webdriver.Chrome, live_server) -> None:
    """
    Tests the loading of website pages and confirms their titles.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        live_server: The live server fixture.

    Returns:
        None. Verifies that all pages exist and their titles match expected values.
    """
    # List of pages to check
    url_titles = [
        {"/users/register": "Registration"},
        {"/users/login": "Log In"},
        {"/index": "Auctions"},
        {"/watchlist": "Watchlist"},
        {"/add_listing": "Add Listing"},
        {"/category/shoes": "Shoes"}
    ]

    for index, item in enumerate(url_titles):
        # Compare expected and actual titles
        url, title = item.popitem()
        navigate_to(driver, live_server, url)
        assert title in driver.title

        # log in after viewing registration and log in pages
        if index == 1:
            login(driver, live_server, LOGIN_USER_FORM_FIELDS)


def test_listings(driver: webdriver.Chrome, live_server) -> None:
    """
    Tests the presence of active listings on the homepage.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        live_server: The live server fixture.

    Returns:
        None. Verifies that the homepage displays active listings by checking for the existence of the item-container class.
    """
    # Navigate to index
    navigate_to(driver, live_server, "/index")

    # Check for auction listing containers
    assert elements_exist(driver, {"class": "item-container"})


def test_category_dropdown(driver: webdriver.Chrome, live_server) -> None:
    """
    Tests the category dropdown functionality.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        live_server: The live server fixture.

    Returns:
        None. Verifies that selecting a category from the active listings page's dropdown redirects the user to the appropriate category page.
    """
    # Check if category dropdown exists
    navigate_to(driver, live_server, "")
    assert elements_exist(driver, {"name": "category"})

    # Select a category and submit choice
    select(driver, "name", "category", "Watches")
    click(driver, "id", "category_select")

    # Verify page loads with the right category
    auctions = find_elements(driver, "class", "item-name")
    assert len(auctions) == 4

    # Verify items match the category
    items = ["Fossil Watch", "Golden Hour Watch", "Casio Watch", "Timex Watch"]
    for auction in auctions:
        assert auction.text in items


def test_validate_registration_form_fields(driver: webdriver.Chrome, live_server) -> None:
    """
    Tests the presence of form fields on the registration form.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        live_server: The live server fixture.

    Returns:
        None. Verifies the presence of all form fields on the registration form.
    """
    # Form fields to check for
    form_fields = {"name": "username", "name": "email", "name": "password", "name": "confirmation", "name": "register"}

    # Navigate to registration
    navigate_to(driver, live_server, "/users/register")

    # Verify elements exist; Selenium will throw NoSuchElementException for any missing element
    assert elements_exist(driver, form_fields)


def test_registration(driver: webdriver.Chrome, live_server) -> None:
    """
    Tests user registration functionality.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        live_server: The live server fixture.

    Returns:
        None. Verifies user registration by attempting to register a new user and checking the displayed greeting after login.
    """
    # Values for form input
    form_fields = {"username": "RegistrationTest", "email": "Testuser@gmail.com", "password": "Register123",
                   "confirmation": "Register123"}

    # Navigate to registration
    driver.get(live_server.url + "/users/register")

    # Enter registration info and submit form
    fill_form(driver, form_fields)
    click(driver, "name", "register")

    # Check expected greeting on index
    expected = "Welcome, RegistrationTest."
    greeting = find_element(driver, "id", "greeting").text
    assert greeting == expected


def test_login_redirect(driver: webdriver.Chrome, live_server) -> None:
    """
    Tests the redirection behavior for a logged-in user visiting the login page.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        live_server: The live server fixture.

    Returns:
        None. Verifies that a logged-in user visiting the login page is redirected to the index.
    """
    # Log in user
    login(driver, live_server, LOGIN_USER_FORM_FIELDS)

    # Navigate to login page
    navigate_to(driver, live_server, "/users/login")

    # Check URL after redirect
    assert live_server.url + "/index" == driver.current_url
