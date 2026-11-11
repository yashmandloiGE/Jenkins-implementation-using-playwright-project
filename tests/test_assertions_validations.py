
from playwright.sync_api import sync_playwright, expect


# Test Case 1: Successful Login Validation
def test_successful_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            page.goto("https://www.saucedemo.com/")

            page.get_by_placeholder("Username").fill("standard_user")
            page.get_by_placeholder("Password").fill("secret_sauce")

            page.get_by_role("button", name="Login").click()

            # Python assertion
            assert "inventory.html" in page.url

            # Playwright assertions
            expect(
                page.get_by_text("Products", exact=True)
            ).to_be_visible()

            expect(
                page.locator(".inventory_item")
            ).to_have_count(6)

        finally:
            browser.close()


# Test Case 2: Invalid Login Validation
def test_invalid_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            page.goto("https://www.saucedemo.com/")

            page.get_by_placeholder("Username").fill("wrong_user")
            page.get_by_placeholder("Password").fill("wrong_password")

            page.get_by_role("button", name="Login").click()

            error = page.locator('[data-test="error"]')

            # Visibility validation
            expect(error).to_be_visible()

            # Text validation
            expect(error).to_contain_text(
                "Username and password do not match"
            )

            # URL validation using Python assertion
            assert "inventory.html" not in page.url

        finally:
            browser.close()
