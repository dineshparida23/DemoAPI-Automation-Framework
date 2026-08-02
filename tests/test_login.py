import allure
import pytest

from schemas.login_schema import login_schema
from utils.assertions import Assertions


@allure.epic("API Automation")
@allure.feature("Login API")
class TestLogin:

    @allure.story("User Login")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "username, password, expected_status",
        [
            (None, None, 200),
            ("admin", "wrongpassword", 401),
            ("wronguser", "admin123", 401),
        ],
    )
    def test_login(self, login_api, username, password, expected_status):

        response = login_api.login(username, password)

        Assertions.verify_status_code(response, expected_status)
        Assertions.verify_response_time(response)

        if expected_status == 200:
            Assertions.verify_schema(response.json(), login_schema)