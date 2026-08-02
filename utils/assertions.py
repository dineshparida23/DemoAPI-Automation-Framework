import allure
from jsonschema import validate


class Assertions:

    @staticmethod
    @allure.step("Verify Status Code = {expected_status}")
    def verify_status_code(response, expected_status):
        assert response.status_code == expected_status, (
            f"Expected {expected_status}, but got {response.status_code}"
        )

    @staticmethod
    @allure.step("Verify Response Time (< 2 sec)")
    def verify_response_time(response):
        assert response.elapsed.total_seconds() < 2, (
            f"Response Time is {response.elapsed.total_seconds()} sec"
        )

    @staticmethod
    @allure.step("Verify JSON Schema")
    def verify_schema(response_json, schema):
        validate(instance=response_json, schema=schema)