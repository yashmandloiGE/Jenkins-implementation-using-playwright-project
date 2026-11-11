
import json
import pytest
from pathlib import Path
from playwright.sync_api import expect


# Load external test data
data_file = Path(__file__).resolve().parents[1] / "test_data" / "login_data.json"

with open(data_file, "r") as file:
    login_data = json.load(file)


@pytest.mark.parametrize("data", login_data)
def test_login_with_external_data(page, data):

    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill(data["username"])
    page.get_by_placeholder("Password").fill(data["password"])

    page.get_by_role("button", name="Login").click()

    if data["expected"] == "success":

        expect(
            page.get_by_text("Products", exact=True)
        ).to_be_visible()

    else:

        expect(
            page.locator('[data-test="error"]')
        ).to_be_visible()
