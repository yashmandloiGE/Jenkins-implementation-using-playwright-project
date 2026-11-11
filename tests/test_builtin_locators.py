
from playwright.sync_api import expect


def test_builtin_locators(page):

    page.goto("https://www.saucedemo.com/")

    # 1. Placeholder locator
    page.get_by_placeholder("Username").fill("standard_user")

    page.get_by_placeholder("Password").fill("secret_sauce")

    # 2. Role locator
    page.get_by_role("button", name="Login").click()

    # 3. Text locator
    expect(
        page.get_by_text("Products", exact=True)
    ).to_be_visible()

    # 4. Role locator for product
    backpack = page.get_by_role(
        "button",
        name="Add to cart"
    ).first

    backpack.click()

    # 5. Text validation
    expect(
        page.get_by_text("Remove", exact=True)
    ).to_be_visible()

    # 6. Verify cart
    expect(
        page.locator(".shopping_cart_badge")
    ).to_have_text("1")
