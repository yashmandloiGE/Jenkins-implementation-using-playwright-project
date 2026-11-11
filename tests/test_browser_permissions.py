
from playwright.sync_api import expect


def test_geolocation_permission(page):

    # Grant location permission
    page.context.grant_permissions(
        ["geolocation"],
        origin="https://www.saucedemo.com"
    )

    # Set mock location
    page.context.set_geolocation({
        "latitude": 19.0760,
        "longitude": 72.8777
    })

    page.goto("https://www.saucedemo.com/")

    # Verify location permission
    permission = page.evaluate("""
        async () => {
            const result = await navigator.permissions.query({
                name: "geolocation"
            });

            return result.state;
        }
    """)

    assert permission == "granted"

    # Verify mocked coordinates
    location = page.evaluate("""
        () => new Promise((resolve, reject) => {
            navigator.geolocation.getCurrentPosition(
                position => resolve({
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude
                }),
                error => reject(error.message)
            );
        })
    """)

    assert location["latitude"] == 19.0760
    assert location["longitude"] == 72.8777

    print("Geolocation permission granted successfully!")
