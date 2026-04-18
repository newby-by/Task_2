import allure
import requests


class UserMethod:

    def __init__(self, url):
        self.url = url

    @allure.step('Register a user with payload={payload}')
    def register(self, payload):
        response = requests.post(
            url=self.url,
            data=payload
        )
        return response
