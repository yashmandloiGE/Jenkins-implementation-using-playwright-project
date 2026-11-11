
from playwright.sync_api import sync_playwright, expect


def test_modern_locator_strategies():

    with sync_playwright() as p:

        # Configure custom test ID attribute
        p.selectors.set_test_id_attribute("data-test")

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            page.goto("https://www.saucedemo.com/")

            # 1. Placeholder locator
            page.get_by_placeholder("Username").fill("standard_user")

            # 2. Role locator
            page.get_by_placeholder("Password").fill("secret_sauce")
            page.get_by_role("button", name="Login").click()

            # 3. Text locator
            expect(
                page.get_by_text("Products", exact=True)
            ).to_be_visible()

            # 4. Test ID locator
            page.get_by_test_id(
                "add-to-cart-sauce-labs-backpack"
            ).click()

            # 5. Filter locator
            backpack = page.locator(".inventory_item").filter(
                has_text="Sauce Labs Backpack"
            )

            # 6. Chained locator
            remove_button = backpack.get_by_role(
                "button",
                name="Remove"
            )

            expect(remove_button).to_be_visible()

            # 7. Verify shopping cart
            expect(
                page.locator(".shopping_cart_badge")
            ).to_have_text("1")

            print("Modern locator strategies verified!")

        finally:
            browser.close()
