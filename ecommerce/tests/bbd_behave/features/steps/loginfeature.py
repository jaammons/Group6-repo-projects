from behave import *
from selenium import webdriver
from utilities import *

LOGIN_USER_FORM_FIELDS = {"username": "User", "password": "testuser1"}
driver = webdriver.Chrome


@given(u'user is on the login page')
def openLoginPage(context):
    context.driver.get("http://127.0.0.1:8000/users/login")


@when(u'valid username and password entered')
def enterCreditenals(context):
    # Fills field with login information
    fill_form(driver, LOGIN_USER_FORM_FIELDS)


@then(u'clicks login button')
def clickLoginButton(context):
    click(driver, "name", "login")  # clicks login


@then(u'user is taken to a new home page')
def openHomePage(context):
    context.driver.get("http://127.0.0.1:8000/index")  # path for the home page
