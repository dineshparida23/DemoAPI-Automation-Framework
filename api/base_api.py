from utils.config_reader import ConfigReader


class BaseAPI:

    def __init__(self, api_client):
        self.api = api_client
        self.config = ConfigReader()