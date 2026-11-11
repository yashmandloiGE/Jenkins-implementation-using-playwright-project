
from playwright.sync_api import expect


def login(page):

    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()


# Test 1: Verify authenticated access
def test_authenticated_access(page):

    login(page)

    expect(
        page.get_by_text("Products", exact=True)
    ).to_be_visible()

    assert "inventory.html" in page.url


# Test 2: Verify unauthenticated access
def test_unauthenticated_access(page):

    page.goto("https://www.saucedemo.com/inventory.html")

    expect(
        page.get_by_placeholder("Username")
    ).to_be_visible()


# Test 3: Verify logout
def test_logout_session(page):

    login(page)

    # Open sidebar menu
    page.locator("#react-burger-menu-btn").click()

    # Locate logout link
    logout_link = page.locator("#logout_sidebar_link")

    # Wait until sidebar logout link becomes visible
    expect(logout_link).to_be_visible(timeout=10000)

    # Click logout
    logout_link.click()

    # Verify logout successful
    expect(
        page.get_by_role("button", name="Login")
    ).to_be_visible()

    print("Logout successful!")
