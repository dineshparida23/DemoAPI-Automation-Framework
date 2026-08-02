import pytest
from fastapi.testclient import TestClient

from main import app

from api.api_client import APIClient
from api.login_api import LoginAPI
from api.users_api import UsersAPI
from api.profile_api import ProfileAPI


@pytest.fixture(scope="module")
def api():
    print("\n========== Module Setup ==========")

    client = TestClient(app)
    api_client = APIClient(client)

    yield api_client

    print("\n========== Module Teardown ==========")


@pytest.fixture(scope="module")
def login_api(api):
    return LoginAPI(api)


@pytest.fixture(scope="module")
def users_api(api):
    return UsersAPI(api)


@pytest.fixture(scope="module")
def profile_api(api):
    return ProfileAPI(api)