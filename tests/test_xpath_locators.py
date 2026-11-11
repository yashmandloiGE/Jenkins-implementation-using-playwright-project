
from playwright.sync_api import expect


def test_xpath_locators(page):

    page.goto("https://www.saucedemo.com/")

    # 1. XPath using ID
    page.locator("//input[@id='user-name']").fill("standard_user")

    # 2. XPath using attribute
    page.locator("//input[@name='password']").fill("secret_sauce")

    # 3. XPath using attribute to click Login
    page.locator("//input[@data-test='login-button']").click()

    # 4. XPath using class
    products = page.locator(
        "//div[@class='inventory_item']"
    )

    expect(products).to_have_count(6)

    # 5. XPath using text and parent-child relationship
    backpack = page.locator(
        "//div[contains(@class,'inventory_item')]"
        "[.//div[text()='Sauce Labs Backpack']]"
        "//button"
    )

    backpack.click()

    # 6. XPath to verify cart
    cart = page.locator(
        "//span[@class='shopping_cart_badge']"
    )

    expect(cart).to_have_text("1")

    print("XPath locators executed successfully!")
