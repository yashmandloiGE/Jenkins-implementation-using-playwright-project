
def login(page, username, password):

    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)

    page.get_by_role("button", name="Login").click()


def add_backpack_to_cart(page):

    page.get_by_test_id(
        "add-to-cart-sauce-labs-backpack"
    ).click()
