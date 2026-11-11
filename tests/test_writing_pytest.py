
from playwright.sync_api import sync_playwright, expect


# Test Case 1: Valid Login
def test_valid_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            page.goto("https://www.saucedemo.com/")

            # Arrange
            page.get_by_placeholder("Username").fill("standard_user")
            page.get_by_placeholder("Password").fill("secret_sauce")

            # Act
            page.get_by_role("button", name="Login").click()

            # Assert
            expect(
                page.get_by_text("Products", exact=True)
            ).to_be_visible()

        finally:
            browser.close()


# Test Case 2: Invalid Login
def test_invalid_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            page.goto("https://www.saucedemo.com/")

            # Arrange
            page.get_by_placeholder("Username").fill("wrong_user")
            page.get_by_placeholder("Password").fill("wrong_password")

            # Act
            page.get_by_role("button", name="Login").click()

            # Assert
            error_message = page.locator('[data-test="error"]')

            expect(error_message).to_be_visible()

        finally:
            browser.close()
