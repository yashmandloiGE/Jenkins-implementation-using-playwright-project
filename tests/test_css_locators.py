
from playwright.sync_api import expect


def test_css_locators(page):

    page.goto("https://www.saucedemo.com/")

    # 1. ID selector
    page.locator("#user-name").fill("standard_user")

    # 2. ID selector
    page.locator("#password").fill("secret_sauce")

    # 3. Attribute selector
    page.locator('[data-test="login-button"]').click()

    # 4. Class selector
    expect(
        page.locator(".inventory_item")
    ).to_have_count(6)

    # 5. Attribute selector
    page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    # 6. Class selector
    expect(
        page.locator(".shopping_cart_badge")
    ).to_have_text("1")

    print("CSS locators executed successfully!")
