
from playwright.sync_api import expect


def test_debug_login(page):

    # Open website
    page.goto("https://www.saucedemo.com/")

    print("Page URL:", page.url)
    print("Page Title:", page.title())

    # Pause execution and open Playwright Inspector
    # page.pause()

    # Login
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()

    # Validate result
    expect(
        page.get_by_text("Products", exact=True)
    ).to_be_visible()

    print("Login debugging completed successfully!")
