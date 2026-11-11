
import json
import os
from pathlib import Path
from playwright.sync_api import expect


# Load environment configuration
config_path = (
    Path(__file__).resolve().parents[1]
    / "config"
    / "environments.json"
)

with open(config_path, "r") as file:
    environments = json.load(file)


# Select environment (default: QA)
environment = os.getenv("TEST_ENV", "qa").lower()

if environment not in environments:
    raise ValueError(f"Unknown environment: {environment}")

config = environments[environment]


def test_environment_configuration(page):

    # Apply environment timeout
    page.set_default_timeout(config["timeout"])

    # Open environment URL
    page.goto(config["base_url"])

    # Validate application
    expect(
        page.get_by_role("button", name="Login")
    ).to_be_visible()

    print("Environment:", environment)
    print("URL:", config["base_url"])
    print("Timeout:", config["timeout"])
