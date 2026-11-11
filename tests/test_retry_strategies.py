
import pytest
from playwright.sync_api import expect

attempt_count = 0


@pytest.mark.flaky(reruns=2)
def test_retry_strategy(page):

    global attempt_count
    attempt_count += 1

    print(f"Execution attempt: {attempt_count}")

    page.set_content("<h1>Checkout Page</h1>")

    # Simulate temporary failure on first attempt
    assert attempt_count >= 2, "Temporary failure occurred"

    expect(
        page.get_by_role("heading", name="Checkout Page")
    ).to_be_visible()

    print("Test passed successfully!")
