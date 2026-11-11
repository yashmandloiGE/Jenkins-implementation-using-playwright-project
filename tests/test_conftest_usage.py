
from playwright.sync_api import expect


# Test Case 1: Verify login page
def test_login_page(page):

    page.goto("https://www.saucedemo.com/")

    expect(
        page.get_by_placeholder("Username")
    ).to_be_visible()

    expect(
        page.get_by_role("button", name="Login")
    ).to_be_visible()


# Test Case 2: Verify successful login
def test_successful_login(page):

    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()

    expect(
        page.get_by_text("Products", exact=True)
    ).to_be_visible()


# Test Case 3: Verify products count
def test_products_count(page):

    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()

    expect(
        page.locator(".inventory_item")
    ).to_have_count(6)
