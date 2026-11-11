
import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_login(page):

    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()

    expect(
        page.get_by_text("Products", exact=True)
    ).to_be_visible()


@pytest.mark.regression
def test_add_product_to_cart(page):

    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()

    page.get_by_test_id(
        "add-to-cart-sauce-labs-backpack"
    ).click()

    expect(
        page.locator(".shopping_cart_badge")
    ).to_have_text("1")


@pytest.mark.sanity
def test_products_page(page):

    page.goto("https://www.saucedemo.com/")

    expect(
        page.get_by_role("button", name="Login")
    ).to_be_visible()
