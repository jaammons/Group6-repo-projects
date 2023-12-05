from behave import then
from when import step_user_looks_for

@then(u'the user greeting is {greeting}')
def step_user_logged_out(context, greeting):
    assert step_user_looks_for(context, "id", "greeting").text == greeting


@then(u'the user is taken to {page}')
def step_user_redirected_to_page(context, page):
    assert context.driver.current_url == "http://127.0.0.1:8000/" + page

@then(u'the user can see element with {selector_type} {selector_value}')
def step_user_can_see(context, selector_type: str, selector_value: str) -> bool:
    """
    Checks if a set of elements exist on the page.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        elements (dict): Dictionary containing selector types and values.

    Returns:
        bool: True if all elements exist, False otherwise.
    """
    assert step_user_looks_for(context, selector_type, selector_value)