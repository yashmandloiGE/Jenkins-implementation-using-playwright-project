
import pytest
from playwright.sync_api import sync_playwright, expect


# Session scope: Browser is created once for the test session
@pytest.fixture(scope="session")
def browser():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        yield browser

        browser.close()


# Function scope: New page for every test
@pytest.fixture(scope="function")
def page(browser):

    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()


# Test Case 1
def test_homepage(page):

    page.set_content("<h1>Welcome to QA Automation</h1>")

    expect(
        page.locator("h1")
    ).to_have_text("Welcome to QA Automation")


# Test Case 2
def test_login_page(page):

    page.set_content("<title>Login Page</title>")

    assert page.title() == "Login Page"
