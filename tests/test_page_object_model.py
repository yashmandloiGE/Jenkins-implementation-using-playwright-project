
from playwright.sync_api import expect
from pages.sauce_demo_page import SauceDemoPage


def test_login_and_add_product(page):

    # Create page object
    sauce = SauceDemoPage(page)

    # Open website
    sauce.open()

    # Login
    sauce.login("standard_user", "secret_sauce")

    # Validate login
    expect(sauce.products_heading).to_be_visible()

    # Add product
    sauce.add_product_to_cart()

    # Validate cart
    expect(sauce.cart_badge).to_have_text("1")

    print("POM test executed successfully!")
