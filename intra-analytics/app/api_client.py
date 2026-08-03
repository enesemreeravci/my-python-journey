import time
from typing import Any

import requests


class FortyTwoAPIError(Exception):
    """Raised when communication with the 42 API fails."""


class FortyTwoClient:
    TOKEN_URL = "https://api.intra.42.fr/oauth/token"
    API_BASE_URL = "https://api.intra.42.fr/v2"

    def __init__(self, client_id: str, client_secret: str) -> None:
        if not client_id or not client_secret:
            raise ValueError("42 API credentials are missing")

        self.client_id = client_id
        self.client_secret = client_secret
        self._access_token: str | None = None
        self._token_expires_at = 0.0

    def _request_access_token(self) -> str:
        response = requests.post(
            self.TOKEN_URL,
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            },
            timeout=10,
        )

        if not response.ok:
            raise FortyTwoAPIError(
                f"Could not obtain access token: {response.status_code}"
            )

        token_data = response.json()

        self._access_token = token_data["access_token"]

        # Refresh slightly before the real expiration time.
        expires_in = token_data.get("expires_in", 7200)
        self._token_expires_at = time.time() + expires_in - 60

        return self._access_token

    def _get_access_token(self) -> str:
        if (
            self._access_token is None
            or time.time() >= self._token_expires_at
        ):
            return self._request_access_token()

        return self._access_token

    def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
    ) -> Any:
        token = self._get_access_token()

        response = requests.get(
            f"{self.API_BASE_URL}{endpoint}",
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
            },
            params=params,
            timeout=10,
        )

        if response.status_code == 404:
            raise FortyTwoAPIError("Resource was not found")

        if not response.ok:
            raise FortyTwoAPIError(
                f"42 API request failed: {response.status_code}"
            )

        return response.json()

    def get_user(self, login: str) -> dict[str, Any]:
        safe_login = login.strip().lower()

        if not safe_login:
            raise ValueError("Login cannot be empty")

        return self.get(f"/users/{safe_login}")