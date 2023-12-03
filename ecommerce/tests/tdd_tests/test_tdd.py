from selenium import webdriver
from time import sleep
from utilities import *
import requests
import pytest

LOGIN_USER_FORM_FIELDS = {"username":"User", "password":"testuser1"}



def test_remember_me(driver, live_server):
    """
    Verifies remember_me checkbox saves a users session.
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
    Verifies session clears when browser is closed if remember_me isn't checked.
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
    Verifies functionality of API get method for retrieving auction data in a json.
    """
    # Create request
    url = live_server.url + "/get"
    params = {"pk":1}

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
    Verifies functionality of API bid method for placing bids on auctions.
    """
    # Create request
    url = live_server.url + "/bids"
    params = {"auction":1, "username": "User", "bid":100}

    # Send request
    response = requests.get(url, params=params)

    # Verify response
    assert response.status_code == 200

def test_bid_display(driver, live_server):
    """
    Verify listings display username if user is currently winning bid.
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