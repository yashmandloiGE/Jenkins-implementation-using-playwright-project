
from playwright.sync_api import expect


def test_hooks_page_heading(page):

    page.set_content("""
        <h1>QA Automation</h1>
    """)

    expect(
        page.get_by_role("heading", name="QA Automation")
    ).to_be_visible()


def test_hooks_button_click(page):

    page.set_content("""
        <button onclick="document.querySelector('p').innerText='Success'">
            Submit
        </button>
        <p>Waiting</p>
    """)

    page.get_by_role("button", name="Submit").click()

    expect(
        page.locator("p")
    ).to_have_text("Success")
