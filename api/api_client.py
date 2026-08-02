from utils.logger import logger
from utils.token_manager import TokenManager


class APIClient:

    def __init__(self, client):
        self.client = client

    def _add_auth_header(self, headers=None):
        """
        Automatically add Authorization header if a JWT token exists.
        """
        token = TokenManager.get_token()

        if token:
            headers = headers or {}
            headers["Authorization"] = f"Bearer {token}"

        return headers

    def get(self, endpoint, auth=False, **kwargs):
        logger.info(f"GET Request -> {endpoint}")

        if auth:
            kwargs["headers"] = self._add_auth_header(
                kwargs.get("headers")
            )

        response = self.client.get(endpoint, **kwargs)

        logger.info(f"Status Code -> {response.status_code}")
        logger.info(f"Response -> {response.text}")

        return response

    def post(self, endpoint, auth=False, **kwargs):
        logger.info(f"POST Request -> {endpoint}")
        logger.info(f"Request Body -> {kwargs}")

        if auth:
            kwargs["headers"] = self._add_auth_header(
                kwargs.get("headers")
            )

        response = self.client.post(endpoint, **kwargs)

        logger.info(f"Status Code -> {response.status_code}")
        logger.info(f"Response -> {response.text}")

        return response

    def put(self, endpoint, auth=False, **kwargs):
        logger.info(f"PUT Request -> {endpoint}")
        logger.info(f"Request Body -> {kwargs}")

        if auth:
            kwargs["headers"] = self._add_auth_header(
                kwargs.get("headers")
            )

        response = self.client.put(endpoint, **kwargs)

        logger.info(f"Status Code -> {response.status_code}")
        logger.info(f"Response -> {response.text}")

        return response

    def delete(self, endpoint, auth=False, **kwargs):
        logger.info(f"DELETE Request -> {endpoint}")

        if auth:
            kwargs["headers"] = self._add_auth_header(
                kwargs.get("headers")
            )

        response = self.client.delete(endpoint, **kwargs)

        logger.info(f"Status Code -> {response.status_code}")
        logger.info(f"Response -> {response.text}")

        return response