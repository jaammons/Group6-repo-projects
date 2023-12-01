from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import pytest

def test_remember_me():
    """
    Verifies remember_me checkbox saves a users session.
    """
    # Navigate to login and click checkbox
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/users/login")
    checkbox = driver.find_element(By.NAME, "remember_me")
    checkbox.click()

    # Login and close browser
    driver.find_element(By.NAME, "username").send_keys("User")
    driver.find_element(By.NAME, "password").send_keys("testuser1")
    driver.find_element(By.NAME, "login").click()
    driver.quit()

    # Return to page and check greeting
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")
    greeting = driver.find_element(By.NAME, "greeting")
    assert greeting.text == "Welcome, User."