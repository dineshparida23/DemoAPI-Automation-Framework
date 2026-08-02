import json
import allure

from api.base_api import BaseAPI
from utils.token_manager import TokenManager


class LoginAPI(BaseAPI):

    @allure.step("Send Login Request")
    def login(self, username=None, password=None):

        if username is None:
            username = self.config.get("username")

        if password is None:
            password = self.config.get("password")

        payload = {
            "username": username,
            "password": password
        }

        allure.attach(
            json.dumps(payload, indent=4),
            name="Request Body",
            attachment_type=allure.attachment_type.JSON
        )

        response = self.api.post(
            "/login",
            data=payload
        )

        allure.attach(
            response.text,
            name="Response Body",
            attachment_type=allure.attachment_type.JSON
        )

        # Save JWT token after successful login
        if response.status_code == 200:
            access_token = response.json()["access_token"]
            TokenManager.set_token(access_token)

        return response