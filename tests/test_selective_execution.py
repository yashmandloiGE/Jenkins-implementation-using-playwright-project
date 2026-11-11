
from playwright.sync_api import expect


def test_login_page(page):

    page.goto("https://www.saucedemo.com/")

    expect(
        page.get_by_role("button", name="Login")
    ).to_be_visible()


def test_valid_login(page):

    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()

    expect(
        page.get_by_text("Products", exact=True)
    ).to_be_visible()


def test_invalid_login(page):

    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("wrong_user")
    page.get_by_placeholder("Password").fill("wrong_password")

    page.get_by_role("button", name="Login").click()

    expect(
        page.locator('[data-test="error"]')
    ).to_be_visible()
