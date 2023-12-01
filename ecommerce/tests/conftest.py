import pytest
from utilities import save_json, display_log
from selenium_tests.test_web_interaction import TestSelenium

def pytest_addoption(parser) -> None:
    parser.addoption("--show", action="store", default="f", help="Customize which test results are displayed. Accepted values\
                     , p, f, s, will display passed, failed, or skipped tests. Ex. --show=ps, will show only passed or skipped tests.")
    
    parser.addoption("--more", action="store_true", default=False, help="Displays additional test details.")

    parser.addoption("--html", action="store_true", default=False, help="Displays an html page with test results.")    


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
        log[name]["doc"] = getattr(TestSelenium(), name).__doc__.strip()
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


    