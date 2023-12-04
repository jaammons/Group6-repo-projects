import pytest
import os
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module", autouse=True)
def browser():
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        yield browser

        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page

def test_page_title(live_server, page):
    page.goto(live_server.url)

    title = page.title()

    assert title == "Auctions"


def test_user_login(live_server, page):
    # Navigate to the specified URL
    page.goto(live_server.url + "/users/login")
    
    # Fill the login form fields
    page.fill('input[name="username"]', 'User')
    page.fill('input[name="password"]', 'testuser1')
    
    # Submit the login form
    page.click('button[type="submit"]')
    
    # Wait for a specific element after login (if applicable)
    # page.wait_for_selector('#greeting')
    
    # Get the greeting message after successful login
    greeting_message = page.inner_text('#greeting')
    
    # Assert the greeting message confirms successful login
    assert greeting_message == 'Welcome, User.'
        