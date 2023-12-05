from behave import when
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

@when(u'the user goes to {url}')
def step_user_navigates_to(context, url: str) -> None:
    """
    Navigates the Chrome WebDriver to a specified URL on the live server.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        live_server: The live server fixture.
        url (str): The URL to navigate to.

    Returns:
        None
    """
    context.driver.get("http://127.0.0.1:8000/" + url)

@when(u'the user fills out {form_name} form')
def step_user_fills_form(context, form_name: str=None) -> None:
    """
    Fills a form with the provided field values.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        form_fields (dict): Dictionary containing field names and their corresponding values.

    Returns:
        None
    """
    # Iterate over form fields
    for field_name, field_value in context.form_fields.items():
        # Enter values
        context.driver.find_element(By.NAME, field_name).send_keys(field_value)


@when(u'the user selects {choice} from the dropdown with {selector_type} {selector_value}')
def step_user_selects_from_dropdown(context, selector_type: str, selector_value: str, choice: str) -> None:
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
    dropdown = step_user_looks_for(context, selector_type, selector_value)
    
    # Select choice
    Select(dropdown).select_by_visible_text(choice)

@when(u'the user clicks on element with {selector_type} {selector_value}')
def step_user_clicks_button(context, selector_type: str, selector_value: str) -> None:
    """
    Clicks on an element identified by the given selector.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        selector_type: The type of selector to use ('id', 'name', 'class').
        selector_value: The value of the selector.

    Returns:
        None
    """
    element = step_user_looks_for(context, selector_type, selector_value)
    element.click()

@when(u'the user looks for web element {selector_type} {selector_value}')
def step_user_looks_for(context, selector_type: str, selector_value: str) -> WebElement:
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
            element = context.driver.find_element(By.ID, selector_value)
        case "name":
            element = context.driver.find_element(By.NAME, selector_value)
        case "class":
            element = context.driver.find_element(By.CLASS_NAME, selector_value)
    return element