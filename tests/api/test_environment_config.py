
import json
import os
import requests
from pathlib import Path


# Load environment configurations
config_path = (
    Path(__file__).resolve().parents[2]
    / "environment_config"
    / "api_environments.json"
)

with open(config_path, "r") as file:
    raw_environments = json.load(file)

# Normalize environment names
environments = {
    key.strip().lower(): value
    for key, value in raw_environments.items()
}

# Select environment
environment = os.getenv("API_ENV", "qa").strip().lower()

if environment not in environments:
    raise ValueError(
        f"Invalid API environment: {environment}. "
        f"Available environments: {list(environments.keys())}"
    )

config = environments[environment]

BASE_URL = config["base_url"]
TIMEOUT = config["timeout"]


def test_api_environment_configuration():

    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=TIMEOUT
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1

    print("Environment:", environment)
    print("API URL:", BASE_URL)
    print("Timeout:", TIMEOUT)
    print("API environment configuration successful!")
