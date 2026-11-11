
from playwright.sync_api import expect


def test_screenshot_on_failure(page):

    page.goto("https://www.saucedemo.com/")

    # Intentionally incorrect assertion to demonstrate
    # automatic screenshot capture

    expect(page.locator("#user-name")).to_have_text(
        "Wrong Username"
    )
