import allure

from utils.assertions import Assertions


@allure.epic("API Automation")
@allure.feature("Profile API")
class TestProfile:

    @allure.story("Get User Profile")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_profile(self, login_api, profile_api):

        # Step 1: Login and save JWT token
        login_api.login()

        # Step 2: Call protected Profile API
        response = profile_api.get_profile()

        # Step 3: Verify response
        Assertions.verify_status_code(response, 200)
        Assertions.verify_response_time(response)

        data = response.json()

        assert data["message"] == "Profile fetched successfully"
        assert data["username"] == "admin"