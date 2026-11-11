
import os

# Website configuration
BASE_URL = os.getenv(
    "BASE_URL",
    "https://www.saucedemo.com/"
)

# Browser configuration
BROWSER_NAME = os.getenv("BROWSER_NAME", "chromium")

HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

# Execution configuration
SLOW_MO = int(os.getenv("SLOW_MO", "500"))

DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))
