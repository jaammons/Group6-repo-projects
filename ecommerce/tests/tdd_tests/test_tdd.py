from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import pytest
from time import sleep
from utilities import reload_page
import requests

def test_remember_me():
    """
    Verifies remember_me checkbox saves a users session.
    """
    # Navigate to login and click checkbox
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/users/login")
    checkbox = driver.find_element(By.NAME, "remember_me")
    checkbox.click()

    # Login User
    driver.find_element(By.NAME, "username").send_keys("User")
    driver.find_element(By.NAME, "password").send_keys("testuser1")
    driver.find_element(By.NAME, "login").click()
    
    # Close page and reopen browser
    driver = reload_page(driver, "http://127.0.0.1:8000")
    
    # Check User greeting
    greeting = driver.find_element(By.ID, "greeting")
    assert greeting.text == "Welcome, User."

def test_dont_remember_me():
    """
    Verifies remember_me checkbox saves a users session.
    """
    # Navigate to login and click checkbox
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/users/login")

    # Login User
    driver.find_element(By.NAME, "username").send_keys("User")
    driver.find_element(By.NAME, "password").send_keys("testuser1")
    
    # Close page and reopen browser
    driver = reload_page(driver, "http://127.0.0.1:8000")
    
    # Check User greeting
    greeting = driver.find_element(By.ID, "greeting")
    assert greeting.text == "Not signed in."

def test_get():
    """
    Verifies functionality of API get method for retrieving auction data in a json.
    """
    # Create request
    url = "http://127.0.0.1:8000/get"
    params = {"pk":1}

    # Send request
    response = requests.get(url, params=params)

    # Verify response
    assert response.status_code == 200

    # Get the data from the response
    data = response.json()
    
    # Check data for valid info
    assert data["pk"] == 1

def test_bid_display(user_driver):
    """
    Verify listings display username if user is currently winning bid.
    """
    # Navigate to auction to bid on
    user_driver.get("http://127.0.0.1:8000/listing/1")

    # Verify notification of winning bid is not currently displayed.
    assert user_driver.find_element(By.ID, "bid_notification").text == "New Bid"

    # Get minimum bid amount needed
    bid = user_driver.find_element(By.ID, "bid")
    min_bid = bid.get_attribute("placeholder")

    # Enter bid
    bid.send_keys(min_bid)

    # Submit bid
    user_driver.find_element(By.ID, "submit_bid").click()

    # Verify notification of user winning bid is displayed.
    assert user_driver.find_element(By.ID, "bid_notification").text == "Currently winning bid."

    # Tell django to reset the bid amount to 40 and change the user
    user_driver.get("http://127.0.0.1:8000/reset_bid")
