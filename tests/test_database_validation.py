import allure

from database.db_utils import Database


@allure.epic("Database Testing")
@allure.feature("API vs Database")
class TestDatabaseValidation:

    @allure.story("Verify User Data")
    def test_user_data(self, users_api):

        # Call API
        response = users_api.get_user_by_id(1)

        assert response.status_code == 200

        api_user = response.json()

        # Query Database
        db = Database()

        db_user = db.get_user_by_id(1)

        db.close()

        # Compare API vs Database
        assert api_user["id"] == db_user[0]
        assert api_user["name"] == db_user[1]
        assert api_user["email"] == db_user[2]