import allure
import json

from utils.token_manager import TokenManager


class ProfileAPI:

    def __init__(self, api_client):
        self.api = api_client

    @allure.step("Get User Profile")
    def get_profile(self):

        token = TokenManager.get_token()

        allure.attach(
            json.dumps(
                {
                    "Authorization": f"Bearer {token}"
                },
                indent=4
            ),
            name="Request Headers",
            attachment_type=allure.attachment_type.JSON
        )

        response = self.api.get(
            "/profile",
            auth=True
        )

        allure.attach(
            response.text,
            name="Response Body",
            attachment_type=allure.attachment_type.JSON
        )

        return response