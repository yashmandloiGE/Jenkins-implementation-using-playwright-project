from playwright.sync_api import sync_playwright


def test_saucedemo_login_with_locators():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=300
        )

        page = browser.new_page()

        try:

            page.goto("https://www.saucedemo.com/")

            # Built-in locator
            username = page.get_by_placeholder("Username")

            # CSS locator
            password = page.locator("#password")

            # XPath locator
            login_button = page.locator(
                "//input[@data-test='login-button']"
            )

            # Validate locators
            assert username.count() == 1
            assert password.count() == 1
            assert login_button.count() == 1

            # Login
            username.fill("standard_user")
            password.fill("secret_sauce")
            login_button.click()

            # Verify successful login
            products = page.get_by_text(
                "Products",
                exact=True
            )

            products.wait_for(state="visible")

            assert products.is_visible()

            print("Login Successful!")

        finally:
            browser.close()