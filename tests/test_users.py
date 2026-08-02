import allure
import pytest

from utils.assertions import Assertions
from utils.excel_reader import ExcelReader


# Read test data from Excel
test_data = ExcelReader.read_data(
    "testdata/users.xlsx",
    "Users"
)


@allure.epic("API Automation")
@allure.feature("Users API")
class TestUsers:

    @allure.story("Get All Users")
    def test_get_all_users(self, users_api):
        response = users_api.get_all_users()

        Assertions.verify_status_code(response, 200)
        Assertions.verify_response_time(response)

        data = response.json()

        assert isinstance(data, list)
        assert len(data) > 0

    @allure.story("Get User By ID")
    @pytest.mark.parametrize(
        "user_id, expected_name",
        test_data
    )
    def test_get_user_by_id(self, users_api, user_id, expected_name):

        response = users_api.get_user_by_id(user_id)

        Assertions.verify_status_code(response, 200)
        Assertions.verify_response_time(response)

        data = response.json()

        assert data["id"] == user_id
        assert data["name"] == expected_name

    @allure.story("User Not Found")
    def test_get_user_not_found(self, users_api):

        response = users_api.get_user_by_id(999)

        Assertions.verify_status_code(response, 404)

        assert response.json()["detail"] == "User not found"

    @allure.story("Create User")
    def test_create_user(self, users_api):

        new_user = {
            "id": 4,
            "name": "Ramesh",
            "email": "ramesh@example.com"
        }

        response = users_api.create_user(new_user)

        Assertions.verify_status_code(response, 201)
        Assertions.verify_response_time(response)

        data = response.json()

        assert data["message"] == "User added successfully"

        user = data["user"]

        assert user["name"] == "Ramesh"
        assert user["email"] == "ramesh@example.com"

    @allure.story("Create User Validation")
    def test_create_user_missing_email(self, users_api):

        new_user = {
            "id": 5,
            "name": "Suresh"
        }

        response = users_api.create_user(new_user)

        Assertions.verify_status_code(response, 422)