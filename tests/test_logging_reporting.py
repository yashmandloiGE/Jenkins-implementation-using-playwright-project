
import logging
from pathlib import Path
from playwright.sync_api import expect


# Create logs folder
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Configure logger
logger = logging.getLogger("QA_Automation")
logger.setLevel(logging.INFO)

if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler = logging.FileHandler(
        log_dir / "test_execution.log",
        encoding="utf-8"
    )

    console_handler = logging.StreamHandler()

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def test_logging_and_reporting(page):

    try:
        logger.info("Opening SauceDemo website")

        page.goto("https://www.saucedemo.com/")

        logger.info("Entering login credentials")

        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")

        logger.info("Clicking login button")

        page.get_by_role("button", name="Login").click()

        logger.info("Verifying successful login")

        expect(
            page.get_by_text("Products", exact=True)
        ).to_be_visible()

        logger.info("Login test passed successfully")

    except Exception:
        logger.exception("Login test failed")
        raise
