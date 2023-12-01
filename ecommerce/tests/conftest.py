import pytest
from utilities import save_json, display_log
from selenium import webdriver
from selenium_tests.test_web_interaction import TestSelenium, login

def pytest_addoption(parser) -> None:
    parser.addoption("--show", action="store", default="f", help="Customize which test results are displayed. Accepted values\
                     , p, f, s, will display passed, failed, or skipped tests. Ex. --show=ps, will show only passed or skipped tests.")
    
    parser.addoption("--more", action="store_true", default=False, help="Displays additional test details.")

    parser.addoption("--html", action="store_true", default=False, help="Displays an html page with test results.")    

@pytest.fixture(scope="session")
def initialize_driver() -> webdriver.Chrome:
    """
    Returns an initialized ChromeDriver.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def driver(initialize_driver: webdriver.Chrome) -> webdriver.Chrome:
    """
    Yields a driver on the homepage, sends logout command after test.
    """
    initialize_driver.get("http://127.0.0.1:8000/")
    yield initialize_driver
    initialize_driver.get("http://127.0.0.1:8000/users/logout")

@pytest.fixture
def user_driver(driver: webdriver.Chrome) -> webdriver.Chrome:
    """
    Returns a ChromeDriver logged in as User on homepage.
    """
    yield login(driver, "User", "testuser1") 

all_test_names = set()
def pytest_collection_modifyitems(config, items) -> None:
    # Get test names from pytest test collection
    global all_test_names
    all_test_names = {item.nodeid[item.nodeid.rfind(":") + 1:] for item in items}

def initialize_log(request) -> dict:
    global all_test_names
    log = {}

    # Initialize dictionary values for all tests
    for name in all_test_names:
        log[name] = {"result":"skip"}
    return log

@pytest.fixture(scope="session", autouse=True, name="log")
def test_log(request) -> dict:
    # Initialize log
    log = initialize_log(request)

    # Yield log and run tests
    yield log 

    # Save test data to a json file
    save_json(log, "test_log")

    # Get command line arguments
    args = []
    args.append(request.config.getoption("--show"))
    args.append(request.config.getoption("--more"))
    
    # Display results
    display_log(log, args)


    