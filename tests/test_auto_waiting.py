
from playwright.sync_api import sync_playwright, expect


def test_playwright_auto_waiting():

    with sync_playwright() as p:

        # Launch browser
        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        try:

            # Create a webpage with a delayed button
            page.set_content("""
                <!DOCTYPE html>
                <html>
                <body>

                    <h2>Auto Waiting Practice</h2>

                    <p id="status">Waiting for submission...</p>

                    <script>

                        // Display button after 1 second
                        setTimeout(() => {

                            const button =
                                document.createElement("button");

                            button.textContent = "Submit";

                            // Initially disable button
                            button.disabled = true;

                            document.body.appendChild(button);

                            // Enable button after another 1 second
                            setTimeout(() => {
                                button.disabled = false;
                            }, 1000);

                            // Handle button click
                            button.addEventListener("click", () => {

                                // Show success message after 1 second
                                setTimeout(() => {

                                    document.querySelector("#status")
                                        .textContent = "Submitted Successfully!";

                                }, 1000);

                            });

                        }, 1000);

                    </script>

                </body>
                </html>
            """)

            print("Webpage opened.")

            # Locate button before it appears
            submit_button = page.get_by_role(
                "button",
                name="Submit"
            )

            print("Waiting for button to become ready...")

            # Playwright automatically waits for:
            # 1. Button to appear
            # 2. Button to become visible
            # 3. Button to become enabled
            # 4. Button to become ready for clicking

            submit_button.click(timeout=5000)

            print("Submit button clicked successfully!")

            # Locate success message
            status = page.locator("#status")

            # Automatically retry assertion until text appears
            expect(status).to_have_text(
                "Submitted Successfully!",
                timeout=5000
            )

            print("Success message verified!")

        finally:
            browser.close()
