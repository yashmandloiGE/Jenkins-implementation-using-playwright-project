
import allure
from playwright.sync_api import expect


@allure.title("Verify successful user login")
@allure.feature("Authentication")
@allure.severity(allure.severity_level.CRITICAL)
def test_allure_login(page):

    with allure.step("Open SauceDemo website"):
        page.goto("https://www.saucedemo.com/")

    with allure.step("Enter login credentials"):
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")

    with allure.step("Click login button"):
        page.get_by_role("button", name="Login").click()

    with allure.step("Verify successful login"):
        expect(
            page.get_by_text("Products", exact=True)
        ).to_be_visible()


@allure.title("Verify product added to cart")
@allure.feature("Shopping Cart")
@allure.severity(allure.severity_level.NORMAL)
def test_allure_add_to_cart(page):

    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()

    with allure.step("Add backpack to cart"):
        page.get_by_test_id(
            "add-to-cart-sauce-labs-backpack"
        ).click()

    with allure.step("Verify cart quantity"):
        expect(
            page.locator(".shopping_cart_badge")
        ).to_have_text("1")
