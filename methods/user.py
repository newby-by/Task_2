import allure

from methods.base_method import BaseMethod


class UserMethod(BaseMethod):

    @allure.step('Register a user with payload={payload}')
    def register(self, payload):
        response = self.post(payload=payload)
        return response

    @allure.step('Login a user with payload={payload}')
    def login(self, payload):
        response = self.post(payload=payload)
        return response
    
    def change_data(self, *, payload=None, headers=None):
        response = self.patch(payload=payload, headers=headers)
        return response
