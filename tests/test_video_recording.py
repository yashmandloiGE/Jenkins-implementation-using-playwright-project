
from pathlib import Path
from playwright.sync_api import expect


def test_video_recording(browser):

    # Create video folder
    video_dir = Path("videos")
    video_dir.mkdir(exist_ok=True)

    # Create context with video recording enabled
    context = browser.new_context(
        record_video_dir=str(video_dir),
        record_video_size={
            "width": 1280,
            "height": 720
        }
    )

    page = context.new_page()

    try:
        # Open website
        page.goto("https://www.saucedemo.com/")

        # Login
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")

        page.get_by_role("button", name="Login").click()

        # Verify login
        expect(
            page.get_by_text("Products", exact=True)
        ).to_be_visible()

        # Add product to cart
        page.get_by_test_id(
            "add-to-cart-sauce-labs-backpack"
        ).click()

        expect(
            page.locator(".shopping_cart_badge")
        ).to_have_text("1")

        print("Video recording completed!")

    finally:
        video = page.video

        # Close context to save the video
        context.close()

        video_path = video.path()

        assert Path(video_path).exists()

        print("Video saved at:", video_path)
