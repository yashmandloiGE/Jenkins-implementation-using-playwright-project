
import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize(
    "username, password, expected_result",
    [
        ("standard_user", "secret_sauce", "success"),
        ("wrong_user", "wrong_password", "failure"),
        ("locked_out_user", "secret_sauce", "failure"),
    ]
)
def test_login_with_multiple_credentials(
    page, username, password, expected_result
):

    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)

    page.get_by_role("button", name="Login").click()

    if expected_result == "success":

        expect(
            page.get_by_text("Products", exact=True)
        ).to_be_visible()

    else:

        expect(
            page.locator('[data-test="error"]')
        ).to_be_visible()
