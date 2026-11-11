
from playwright.sync_api import sync_playwright, expect


def test_playwright_execution_model():

    # 1. Start Playwright
    with sync_playwright() as p:

        # 2. Launch browser
        browser = p.chromium.launch(headless=False)

        try:
            # 3. Create browser context
            context = browser.new_context()

            # 4. Create page
            page = context.new_page()

            # 5. Execute browser operations
            page.set_content("""
                <html>
                    <head>
                        <title>Execution Model</title>
                    </head>
                    <body>
                        <h1 id="message">Ready</h1>
                        <button onclick="
                            document.getElementById('message')
                            .innerText = 'Execution Completed'
                        ">
                            Run
                        </button>
                    </body>
                </html>
            """)

            # 6. Execute JavaScript in browser
            browser_title = page.evaluate("document.title")

            print("Browser title:", browser_title)

            # 7. Perform interaction
            page.get_by_role("button", name="Run").click()

            # 8. Validate result
            expect(page.locator("#message")).to_have_text(
                "Execution Completed"
            )

            print("Playwright execution successful!")

            context.close()

        finally:
            # 9. Close browser
            browser.close()
