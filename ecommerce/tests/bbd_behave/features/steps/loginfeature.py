from behave import *
from selenium import webdriver


@given(u'user is on the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given user is on the login page')


@when(u'valid username and password entered')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When valid username and password entered')


@then(u'clicks login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then clicks login button')


@then(u'user is taken to a new login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user is taken to a new login page')
