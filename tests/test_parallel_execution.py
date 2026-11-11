
from playwright.sync_api import expect


def login(page):

    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()


# Test 1
def test_login(page):

    login(page)

    expect(
        page.get_by_text("Products", exact=True)
    ).to_be_visible()


# Test 2
def test_products_count(page):

    login(page)

    expect(
        page.locator(".inventory_item")
    ).to_have_count(6)


# Test 3
def test_add_to_cart(page):

    login(page)

    page.get_by_test_id(
        "add-to-cart-sauce-labs-backpack"
    ).click()

    expect(
        page.locator(".shopping_cart_badge")
    ).to_have_text("1")


# Test 4
def test_cart_page(page):

    login(page)

    page.get_by_test_id(
        "shopping-cart-link"
    ).click()

    expect(
        page.get_by_text("Your Cart")
    ).to_be_visible()
