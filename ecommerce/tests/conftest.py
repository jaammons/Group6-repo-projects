from django.core.management import call_command
from utilities import capture_screenshot
from selenium import webdriver
import pytest                               

def pytest_addoption(parser) -> None:
    parser.addoption("--screenshot", action="store_true", default=False, help="Takes a screenshot at the end of each test.")

# scope variable determines how often to run the fixture. Session is once per testing session.
@pytest.fixture(scope='function', autouse=True)
def django_db_setup(django_db_setup, django_db_blocker):
   # Open database and populate data
   with django_db_blocker.unblock():
      call_command("flush", interactive=False)
      call_command('loaddata', 'default.json')

@pytest.fixture(scope="session")
def driver(live_server) -> webdriver.Chrome:
   # Create chromedriver instance
   driver = webdriver.Chrome()
   yield driver
   # End chromedriver instance
   driver.quit()

@pytest.fixture(scope="function", autouse=True)
def screenshot(request, driver):
    yield
    # Get the name of the test function
    function_name = request.function.__name__

    # Take screenshot if --screenshot in command line arguments
    if request.config.getoption("--screenshot"):
        capture_screenshot(driver, function_name)

    # Take screenshot if test failed
    elif not request.session.testsfailed:
        capture_screenshot(driver, function_name + "_actual")