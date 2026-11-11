
import pytest
from playwright.sync_api import expect


attempt_count = 0


@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_retry_mechanism(page):

    global attempt_count
    attempt_count += 1

    print(f"Test attempt: {attempt_count}")

    page.set_content("""
        <h1>QA Automation</h1>
    """)

    # Simulate temporary failure on first attempt
    assert attempt_count >= 2, "Simulated temporary failure"

    # Validate successful retry
    expect(
        page.locator("h1")
    ).to_have_text("QA Automation")

    print("Test passed after retry!")
