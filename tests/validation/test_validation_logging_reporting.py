
import requests
import logging
from pathlib import Path


BASE_URL = "https://jsonplaceholder.typicode.com"


# Create logs folder
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Configure logger
logger = logging.getLogger("API_Testing")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler = logging.FileHandler(
        log_dir / "api_execution.log",
        encoding="utf-8"
    )

    console_handler = logging.StreamHandler()

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def test_api_logging_and_reporting():

    try:
        # Send GET request
        logger.info("Sending GET request")

        response = requests.get(
            f"{BASE_URL}/posts/1",
            timeout=15
        )

        logger.info(f"Status Code: {response.status_code}")

        # Validate status code
        assert response.status_code == 200

        logger.info("Status code validation passed")

        # Extract response data
        data = response.json()

        logger.info(f"Response Post ID: {data['id']}")

        # Validate response data
        assert data["id"] == 1

        logger.info("Response data validation passed")
        logger.info("API test completed successfully")

    except Exception:

        logger.exception("API test failed")
        raise
