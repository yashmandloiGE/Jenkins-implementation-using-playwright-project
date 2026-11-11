
from playwright.sync_api import sync_playwright


# Test case 1
def test_page_title():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            page.set_content("<title>My QA Website</title>")

            assert page.title() == "My QA Website"

        finally:
            browser.close()


# Test case 2
def test_page_heading():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            page.set_content("<h1>Welcome to Playwright</h1>")

            heading = page.locator("h1")

            assert heading.inner_text() == "Welcome to Playwright"

        finally:
            browser.close()
