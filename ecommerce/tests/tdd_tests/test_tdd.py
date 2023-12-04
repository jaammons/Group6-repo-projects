from selenium import webdriver
from time import sleep
from utilities import *
import requests
import pytest

LOGIN_USER_FORM_FIELDS = {"username": "User", "password": "testuser1"}


def test_remember_me(driver, live_server):
    """
    Verifies that the 'remember_me' checkbox saves a user's session.

    Args:
        driver (webdriver): The WebDriver instance.
        live_server: The live server fixture.

    Returns:
        None. Verifies that the session cookie won't expire on browser close if 'remember_me' is checked.
    """
    # Navigate to login
    navigate_to(driver, live_server, "/users/login")

    # Click checkbox
    click(driver, "name", "remember_me")

    # Login User
    fill_form(driver, LOGIN_USER_FORM_FIELDS)
    click(driver, "name", "login")

    # Check that cookie won't expire on browser close
    assert get_cookie_expiration_time(driver, "sessionid") > 0


def test_dont_remember_me(driver, live_server):
    """
    Verifies that the session clears when the browser is closed if 'remember_me' isn't checked.

    Args:
        driver (webdriver): The WebDriver instance.
        live_server: The live server fixture.

    Returns:
        None. Verifies that the session cookie expires on browser close if 'remember_me' is not checked.
    """
    # Navigate to login
    navigate_to(driver, live_server, "/users/login")

    # Login User
    fill_form(driver, LOGIN_USER_FORM_FIELDS)
    click(driver, "name", "login")

    # Check that cookie expires on browser close
    assert get_cookie_expiration_time(driver, "sessionid") == 0


def test_get(live_server):
    """
    Verifies the functionality of the API GET method for retrieving auction data in JSON.

    Args:
        live_server: The live server fixture.

    Returns:
        None. Verifies the response status code and checks the retrieved JSON data for valid information.
    """
    # Create request
    url = live_server.url + "/get"
    params = {"pk": 1}

    # Send request
    response = requests.get(url, params=params)

    # Verify response
    assert response.status_code == 200

    # Get the data from the response
    data = response.json()

    # Check data for valid info
    assert data["pk"] == 1


def test_bid_api(live_server):
    """
    Verifies the functionality of the API BID method for placing bids on auctions.

    Args:
        live_server: The live server fixture.

    Returns:
        None. Verifies the response status code.
    """
    # Create request
    url = live_server.url + "/bids"
    params = {"auction": 1, "username": "User", "bid": 100}

    # Send request
    response = requests.get(url, params=params)

    # Verify response
    assert response.status_code == 200


def test_bid_display(driver, live_server):
    """
    Verifies that listings display the username if the user is currently winning the bid.

    Args:
        driver (webdriver): The WebDriver instance.
        live_server: The live server fixture.

    Returns:
        None. Verifies the display of a notification indicating the winning bid status on the auction page.
    """
    # Log in user
    login(driver, live_server, LOGIN_USER_FORM_FIELDS)

    # Navigate to auction to bid on
    navigate_to(driver, live_server, "/listing/1")

    # Verify notification of winning bid is not currently displayed.
    assert find_element(driver, "id", "bid_notification").text == "New Bid"

    # Get minimum bid amount needed
    bid = find_element(driver, "id", "bid")
    min_bid = bid.get_attribute("placeholder")

    # Enter bid
    bid.send_keys(min_bid)
    # Submit bid
    click(driver, "id", "submit_bid")

    # Verify notification of user winning bid is displayed.
    assert find_element(driver, "id", "bid_notification").text == "Currently winning bid."
