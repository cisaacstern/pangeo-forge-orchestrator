from dataclasses import dataclass
from typing import Optional

# mypy says stubs not installed but they are... hmm...
import requests  # type: ignore


@dataclass
class Client:
    """A client for the Pangeo Forge database API. Full API documentation, including available
    endpoints and JSON request formatting, is available at the ``'/docs/'`` and/or ``'/redoc/'``
    routes of the API. Currently the only attribute all methods in this ``Client`` share is a
    ``base_url``, but this may expand in the future to include credentials, etc.

    :param base_url: The base URL for the API (without a trailing forward slash). If running a
    local API development server with ``uvicorn``, this is likely to be ``'http://127.0.0.1:8000'``.
    :param api_key: An optional authorization key, which will be used for the x-api-key HTTP header.
    """

    base_url: str
    api_key: Optional[str] = None

    def __post_init__(self):
        self.session = requests.Session()
        if self.api_key is not None:
            header = {"x-api-key": self.api_key}
            self.session.headers.update(header)

    def post(self, endpoint: str, json: dict):
        """Add new entries to the database.

        :param endpoint: A top level endpoint, enclosed in forward slashes, e.g. '/my_endpoint/'.
        :param json: The request JSON as a Python ``dict``.
        """
        response = self.session.post(f"{self.base_url}{endpoint}", json=json)
        response.raise_for_status()
        return response

    def get(self, endpoint: str):
        """Read entries from the database.

        :param endpoint: Either a top level endpoint, enclosed in forward slashes, e.g.
            '/my_endpoint/'. Or a unique entry endpoint concluding with an integer id, e.g.
            '/my_endpoint/1'. If the former, returns list of all entries in corresponding
            table. If the latter, returns single table entry.
        """
        response = self.session.get(f"{self.base_url}{endpoint}")
        response.raise_for_status()
        return response

    def patch(self, endpoint: str, json: dict):
        """Update entries in the database.

        :param endpoint: A top level endpoint, enclosed in forward slashes, e.g. '/my_endpoint/'.
        :param json: The request JSON as a Python ``dict``.
        """
        response = self.session.patch(f"{self.base_url}{endpoint}", json=json)
        response.raise_for_status()
        return response

    def delete(self, endpoint: str):
        """Delete entries from the database.

        :param endpoint: A unique entry endpoint concluding with an integer id,
            e.g. '/my_endpoint/1'.
        """
        response = self.session.delete(f"{self.base_url}{endpoint}")
        response.raise_for_status()
        return response
