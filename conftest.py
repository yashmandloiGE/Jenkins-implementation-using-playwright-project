from utils.sauce_demo_helpers import login
from config import BROWSER_NAME, HEADLESS, SLOW_MO
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright


# Browser fixture
@pytest.fixture(scope="session")
def browser():

    with sync_playwright() as p:

        p.selectors.set_test_id_attribute("data-test")

        browser = p.chromium.launch(
            headless=False,
            slow_mo=500
        )

        yield browser

        browser.close()


# Page fixture
@pytest.fixture(scope="function")
def page(browser):

    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()


# Screenshot on test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page and not page.is_closed():

            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            filename = item.name.replace("/", "_").replace("\\", "_")

            screenshot_path = screenshot_dir / f"{filename}.png"

            try:
                page.screenshot(
                    path=str(screenshot_path),
                    full_page=True
                )

                print(f"\nScreenshot saved: {screenshot_path}")

            except Exception as error:
                print(f"\nScreenshot capture failed: {error}")

@pytest.fixture
def logged_in_page(page):

    login(page, "standard_user", "secret_sauce")

    return page