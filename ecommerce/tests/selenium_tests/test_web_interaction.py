from selenium import webdriver
from utilities import *   
from time import sleep

import pytest

LOGIN_USER_FORM_FIELDS = {"username":"User", "password":"testuser1"}
REGISTRATION_FORM_FIELDS = {"username":"RegistrationTest", "email":"Testuser@gmail.com", "password":"Register123"
                            , "confirmation":"Register123"}


def test_login(driver: webdriver.Chrome, live_server) -> None:
    """
    Verifies log in functionality by attempting to log in a user and checking greeting on index after log in attempt. 
    Expected result: User is logged in.
    """
    # Log in as User
    login(driver, live_server, LOGIN_USER_FORM_FIELDS)

    # Verify expected greeting on index
    expected = "Welcome, User."  # Output is Welcome, <username>, but the test user is User.
    greeting = find_element(driver, "id", "greeting").text
    assert greeting == expected


def test_logout(driver: webdriver.Chrome, live_server) -> None:
    """
    Verifies log out was successful by checking user greeting on index after log out attempt.
    Expected result: User is logged out.
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
    Verifies the ability to load all the website pages and confirms their titles are correct.
    Expected result: All pages exist and titles match key values.
    """
    # List of pages to check
    url_titles = [{"/users/register":"Registration"}, {"/users/login":"Log In"}, {"/index":"Auctions"}, {"/watchlist":"Watchlist"}
                  , {"/add_listing":"Add Listing"}, {"/category/shoes":"Shoes"}]
    
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
    Verifies that the homepage is showing active listings by searching for the listing container class name in the django template.
    Expected result: item-container class exists.
    """
    # Navigate to index
    navigate_to(driver, live_server, "/index")

    # Check for auction listing containers
    assert elements_exist(driver, {"class":"item-container"})

def test_category_dropdown(driver: webdriver.Chrome, live_server) -> None:
    """
    Verifies category dropdown selection from active listings page redirects user to the appropriate category.
    Expected outcome: User redirected to selected category page.
    """
    # Check if category dropdown exists
    navigate_to(driver, live_server, "")
    assert elements_exist(driver, {"name":"category"})

    # Select a category and submit choice
    select(driver, "name", "category", "Watches")
    click(driver, "id", "category_select")

    # Verify page loads with right category
    auctions = find_elements(driver, "class", "item-name")
    assert len(auctions) == 4

    # Verify items match category
    items = ["Fossil Watch", "Golden Hour Watch", "Casio Watch", "Timex Watch"]
    for auction in auctions:
        assert auction.text in items

def test_validate_registration_form_fields(driver: webdriver.Chrome, live_server) -> None:
    """
    Verifies all form fields are present on registration form.
    Expected result: All fields are present.
    """
    # Form fields to check for
    form_fields = {"name":"username","name":"email","name":"password","name":"confirmation","name":"register"}

    # Navigate to registration
    navigate_to(driver, live_server, "/users/register")

    # Verify elements exist, selenium will throw NoSuchElementException for any missing element
    assert elements_exist(driver, form_fields)
  
   
def test_registration(driver: webdriver.Chrome, live_server) -> None:
    """
    Verifies user registration by attempting to register a new user and checking the user greeting after login.
    """
    # Values for form input
    form_fields = {"username":"RegistrationTest", "email":"Testuser@gmail.com", "password":"Register123"
                    , "confirmation":"Register123"}
   
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
    Verifies that a logged in user visiting the log in page is redirected to the index.
    """
    # Log in user
    login(driver, live_server, LOGIN_USER_FORM_FIELDS)

    # Navigate to log in page
    navigate_to(driver, live_server, "/users/login")

    # Check url after redirect
    assert live_server.url + "/index" == driver.current_url