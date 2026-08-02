from api.base_api import BaseAPI


class UsersAPI(BaseAPI):

    def get_all_users(self):
        return self.api.get("/users")

    def get_user_by_id(self, user_id):
        return self.api.get(f"/users/{user_id}")

    def create_user(self, user_data):
        return self.api.post(
            "/users",
            json=user_data
        )

    def update_user(self, user_id, user_data):
        return self.api.put(
            f"/users/{user_id}",
            json=user_data
        )

    def delete_user(self, user_id):
        return self.api.delete(f"/users/{user_id}")