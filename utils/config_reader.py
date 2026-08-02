import os
import json
from dotenv import load_dotenv

load_dotenv()


class ConfigReader:

    def __init__(self):
        with open("config/config.json", "r") as file:
            self.config = json.load(file)

    def get(self, key):
        env_mapping = {
            "username": "API_USERNAME",
            "password": "API_PASSWORD",
            "base_url": "BASE_URL",
            "timeout": "TIMEOUT"
        }

        env_key = env_mapping.get(key)

        if env_key:
            env_value = os.getenv(env_key)
            if env_value is not None:
                return env_value

        return self.config.get(key)