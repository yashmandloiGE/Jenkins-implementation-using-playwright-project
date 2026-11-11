
from pathlib import Path
from playwright.sync_api import expect


def test_trace_viewer(page):

    # Create trace folder
    trace_dir = Path("traces")
    trace_dir.mkdir(exist_ok=True)

    # Start recording
    page.context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    try:
        # Open website
        page.goto("https://www.saucedemo.com/")

        # Login
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")

        page.get_by_role("button", name="Login").click()

        # Validate Products page
        expect(
            page.get_by_text("Products", exact=True)
        ).to_be_visible()

        print("Test execution completed!")

    finally:
        # Save trace file
        page.context.tracing.stop(
            path=str(trace_dir / "trace_viewer.zip")
        )

        print("Trace saved successfully!")
