
from playwright.sync_api import expect
from utils.sauce_demo_helpers import add_backpack_to_cart


# Test 1: Verify available products
def test_products_using_fixture(logged_in_page):

    expect(
        logged_in_page.locator(".inventory_item")
    ).to_have_count(6)


# Test 2: Verify reusable cart utility
def test_add_product_using_utility(logged_in_page):

    add_backpack_to_cart(logged_in_page)

    expect(
        logged_in_page.locator(".shopping_cart_badge")
    ).to_have_text("1")
