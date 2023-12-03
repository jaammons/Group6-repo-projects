from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import json

def select(driver: webdriver.Chrome, selector_type: str, selector_value: str, choice: str) -> None:
    """
    Selects an option in a dropdown by visible text.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        selector_type (str): The type of selector to use ('id', 'name', 'class').
        selector_value (str): The value of the selector.
        choice (str): The visible text of the option to select.

    Returns:
        None
    """
    # Find dropdown menu
    dropdown = find_element(driver, selector_type, selector_value)
    
    # Select choice
    Select(dropdown).select_by_visible_text(choice)

def fill_form(driver: webdriver.Chrome, form_fields: dict) -> None:
    """
    Fills a form with the provided field values.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        form_fields (dict): Dictionary containing field names and their corresponding values.

    Returns:
        None
    """
    # Iterate over form fields
    for field_name, field_value in form_fields.items():
        # Enter values
        driver.find_element(By.NAME, field_name).send_keys(field_value)

def click(driver: webdriver.Chrome, selector_type, selector_value) -> None:
    """
    Clicks on an element identified by the given selector.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        selector_type: The type of selector to use ('id', 'name', 'class').
        selector_value: The value of the selector.

    Returns:
        None
    """
    element = find_element(driver, selector_type, selector_value)
    element.click()

def navigate_to(driver: webdriver.Chrome, live_server, url: str) -> None:
    """
    Navigates the Chrome WebDriver to a specified URL on the live server.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        live_server: The live server fixture.
        url (str): The URL to navigate to.

    Returns:
        None
    """
    driver.get(live_server.url + url)

def find_element(driver: webdriver.Chrome, selector_type: str, selector_value: str) -> WebElement:
    """
    Finds and returns a WebElement using the provided selector.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        selector_type (str): The type of selector to use ('id', 'name', 'class').
        selector_value (str): The value of the selector.

    Returns:
        WebElement: The found WebElement. Not found returns None.
    """
    element = None
    # Find element by given css selector
    match selector_type:
        case "id":
            element = driver.find_element(By.ID, selector_value)
        case "name":
            element = driver.find_element(By.NAME, selector_value)
        case "class":
            element = driver.find_element(By.CLASS_NAME, selector_value)
    return element

def find_elements(driver: webdriver.Chrome, selector_type: str, selector_value: str) -> WebElement:
    """
    Finds and returns a list of WebElements using the provided selector.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        selector_type (str): The type of selector to use ('id', 'name', 'class').
        selector_value (str): The value of the selector.

    Returns:
        WebElement: The found WebElement. Not found returns None.
    """
    elements = None
    # Find elements by given css selector
    match selector_type:
        case "id":
            elements = driver.find_elements(By.ID, selector_value)
        case "name":
            elements = driver.find_elements(By.NAME, selector_value)
        case "class":
            elements = driver.find_elements(By.CLASS_NAME, selector_value)
    return elements

def elements_exist(driver: webdriver.Chrome, elements: dict) -> bool:
    """
    Checks if a set of elements exist on the page.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        elements (dict): Dictionary containing selector types and values.

    Returns:
        bool: True if all elements exist, False otherwise.
    """
    # Iterate over items
    for selector_type, selector_value in elements.items():
        # Find next element
        elements = find_elements(driver, selector_type, selector_value)
        # Check if any of current element exist
        if len(find_elements(driver, selector_type, selector_value)) == 0:
            return False
    return True

def login(driver: webdriver.Chrome, live_server, form_fields: dict) -> webdriver.Chrome:
    """
    Navigates chromedriver to login page and submits login form with given arguments.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        live_server: The live server fixture.
        form_fields (dict): Dictionary containing field names and their corresponding values.

    Returns:
        webdriver.Chrome: The updated Chrome WebDriver instance.
    """
    navigate_to(driver, live_server, "/users/login")
    fill_form(driver, form_fields)
    click(driver, "name", "login")

def capture_screenshot(driver: webdriver.Chrome, file_name: str):
    """
    Capture a screenshot of the current webpage selenium driver is on and save it
    to file using file_name.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        file_name (str): The name of the screenshot file.

    Returns:
        None
    """
    driver.save_screenshot("auctions/static/tests/" + file_name + ".png")

def save_json(data: dict, file_name: str) -> None:
    """
    Save the passed data as file_name.json.

    Args:
        data (dict): The data to be saved.
        file_name (str): The name of the JSON file.

    Returns:
        None
    """
    with open(file_name,"w") as json_file:
        json.dump(data, json_file, indent=4)

def read_json(file_name: str) -> dict:
    """
    Reads data from file_name.json and returns a dict.

    Args:
        file_name (str): The name of the JSON file.

    Returns:
        dict: The data read from the JSON file.
    """
    with open(file_name,"r") as json_file:
        data = json.loads(json_file)
        return data

def get_cookie_expiration_time(driver, cookie_name):
    """
    Gets the expiration time of a specific cookie.

    Args:
        driver: The Chrome WebDriver instance.
        cookie_name (str): The name of the cookie.

    Returns:
        int: The expiration time of the cookie.
    """
    # Get all cookies
    cookies = driver.get_cookies()

    # Find the specific cookie by name
    target_cookie = next((cookie for cookie in cookies if cookie["name"] == cookie_name), None)

    # Extract and return the expiration time of the cookie
    if target_cookie:
        if "expiry" in target_cookie:
            return target_cookie["expiry"]

    return 0
