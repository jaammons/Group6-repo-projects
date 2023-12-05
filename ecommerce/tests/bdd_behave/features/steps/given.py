from behave import given
from selenium import webdriver
from when import *

LOGIN_USER_FORM_FIELDS = {"username": "User", "password": "testuser1"}
REGISTRATION_FORM_FIELDS = {"username": "RegistrationTest", "email": "Testuser@gmail.com", "password": "Register123", "confirmation": "Register123"}


@given(u'the user is on {page}')
def step_user_is_on_page(context, page: str) -> None:
    context.driver.get("http://127.0.0.1:8000/" + page)

@given(u'the user has {item}')
def step_user_has(context, item: str) -> None:
    match item:
        case "valid log in credentials":
            context.form_fields = LOGIN_USER_FORM_FIELDS
        case "valid registration information":
            context.form_fields = REGISTRATION_FORM_FIELDS
            
@given(u'the user is logged in')
def step_login_user(context) -> None:
    """
    Navigates chromedriver to login page and submits login form with given arguments.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver instance.
        live_server: The live server fixture.
        form_fields (dict): Dictionary containing field names and their corresponding values.

    Returns:
        webdriver.Chrome: The updated Chrome WebDriver instance.
    """
    context.form_fields = LOGIN_USER_FORM_FIELDS
    step_user_has(context, "valid log in credentials")
    step_user_navigates_to(context, "users/login")
    step_user_fills_form(context)
    step_user_clicks_button(context, "name", "login")