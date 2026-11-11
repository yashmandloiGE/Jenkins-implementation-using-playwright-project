
from config import BASE_URL, DEFAULT_TIMEOUT
from playwright.sync_api import expect


def test_framework_configuration(page):

    # Apply configured timeout
    page.set_default_timeout(DEFAULT_TIMEOUT)

    # Open configured website
    page.goto(BASE_URL)

    # Verify website
    expect(
        page.get_by_role("button", name="Login")
    ).to_be_visible()

    print("Website URL:", BASE_URL)
    print("Default timeout:", DEFAULT_TIMEOUT)
    print("Framework configuration verified!")
