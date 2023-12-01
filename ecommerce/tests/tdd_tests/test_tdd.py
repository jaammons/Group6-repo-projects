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

def test_get_auction():
    """
    Verifies functionality of API get method for retrieving auction data in a json.
    """
    # Create request
    url = "http://127.0.0.1:8000/auctions"
    params = {"get":1}

    # Send request
    response = requests.get(url, params=params)

    # Verify response
    assert response.status_code == 200