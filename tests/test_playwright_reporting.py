
from playwright.sync_api import expect


def test_homepage_reporting(page):

    page.set_content("""
        <h1>QA Automation</h1>
        <button>Login</button>
    """)

    expect(
        page.get_by_role("heading", name="QA Automation")
    ).to_be_visible()


def test_button_reporting(page):

    page.set_content("""
        <button onclick="this.innerText='Logged In'">
            Login
        </button>
    """)

    page.get_by_role("button", name="Login").click()

    expect(
        page.get_by_role("button", name="Logged In")
    ).to_be_visible()


def test_title_reporting(page):

    page.set_content("<title>Playwright Testing</title>")

    assert page.title() == "Playwright Testing"
