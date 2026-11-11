
def test_multiple_tabs_and_sessions(page, browser):

    # Create first tab
    page.goto("https://www.saucedemo.com/")

    # Get existing browser context
    context = page.context

    # Add a session cookie
    context.add_cookies([
        {
            "name": "qa_session",
            "value": "shared_session",
            "url": "https://www.saucedemo.com/"
        }
    ])

    # Create second tab in the same session
    second_tab = context.new_page()

    second_tab.goto("https://www.saucedemo.com/")

    # Verify cookie is shared between tabs
    assert "qa_session=shared_session" in second_tab.evaluate(
        "document.cookie"
    )

    # Create a separate browser session
    new_context = browser.new_context()

    try:
        third_tab = new_context.new_page()

        third_tab.goto("https://www.saucedemo.com/")

        # Verify separate session does not share cookies
        assert "qa_session=shared_session" not in third_tab.evaluate(
            "document.cookie"
        )

        print("Multiple tabs handled successfully!")
        print("Session isolation verified!")

    finally:
        new_context.close()
