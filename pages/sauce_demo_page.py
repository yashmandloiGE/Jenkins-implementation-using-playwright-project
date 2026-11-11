
from config import BASE_URL


class SauceDemoPage:

    def __init__(self, page):

        self.page = page

        # Locators
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.products_heading = page.get_by_text("Products", exact=True)

        self.add_backpack = page.get_by_test_id(
            "add-to-cart-sauce-labs-backpack"
        )

        self.cart_badge = page.locator(".shopping_cart_badge")

    # Page actions
    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def add_product_to_cart(self):
        self.add_backpack.click()
