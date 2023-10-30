from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture
def driver():
    """
    Returns a ChromeDriver with index.html open.
    """
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/")
    yield driver

@pytest.fixture
def admin_driver():
    """
    Returns a ChromeDriver logged in as Admin on index.html.
    """
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/users/login")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("Admin")
    driver.find_element(By.NAME, "login").click()
    yield driver

def test_login(admin_driver):
    """
    Test verifies admin_driver log in was successful by checking user greeting
    on index.html after log in attempt.
    Expected result: Admin is logged in.
    """
    greeting = admin_driver.find_element(By.ID, "greeting")
    assert greeting.text == "Welcome, Admin."

def test_logout(admin_driver):
    """
    Test verifies log out was successful by checking user greeting
    on index.html after log out attempt.
    Expected result: User is logged out.
    """
    admin_driver.find_element(By.ID, "logout").click()
    greeting = admin_driver.find_element(By.ID, "greeting")
    assert greeting.text == "Not signed in."
    