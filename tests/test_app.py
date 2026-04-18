"""Contract tests for the user preference service."""

import unittest

from user_preference_api.main import create_app


class UserPreferenceApiTests(unittest.TestCase):
    """Verify the user preference service contract."""

    def test_root_returns_hello_world(self) -> None:
        """The root endpoint returns the demo payload."""
        client = create_app().test_client()

        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "hello world"})

    def test_health_returns_ok(self) -> None:
        """The service exposes a basic health endpoint."""
        client = create_app().test_client()

        response = client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {"service": "user-preference-api", "status": "ok"},
        )
