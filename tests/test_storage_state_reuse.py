
from playwright.sync_api import expect


def test_storage_state_reuse(page, browser, tmp_path):

    # Step 1: Login
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()

    expect(
        page.get_by_text("Products", exact=True)
    ).to_be_visible()

    # Step 2: Save authentication state
    state_file = tmp_path / "auth_state.json"

    page.context.storage_state(
        path=str(state_file)
    )

    print("Authentication state saved!")

    # Step 3: Create a new context using saved state
    new_context = browser.new_context(
        storage_state=str(state_file)
    )

    try:
        new_page = new_context.new_page()

        # Step 4: Open protected page without login
        new_page.goto(
            "https://www.saucedemo.com/inventory.html"
        )

        # Step 5: Verify authenticated access
        expect(
            new_page.get_by_text("Products", exact=True)
        ).to_be_visible()

        assert "inventory.html" in new_page.url

        print("Storage state reused successfully!")
        print("Access granted without logging in again!")

    finally:
        new_context.close()
