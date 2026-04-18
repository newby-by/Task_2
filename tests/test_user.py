from http import HTTPStatus

import allure
import pytest

import data
from methods.user import UserMethod


@allure.feature('User API')
class TestUser:

    @allure.title('Create a user')
    @allure.description('All data are expected {user_with_all_data}')
    def test_create_user_with_all_expected_data(self, user_with_all_data):
        response = UserMethod(data.REGISTER_URL).register(
            payload=user_with_all_data
        )
        user = response.json().get('user', False)
        with allure.step('Checking the body of response {response.text}'):
            assert (
                response.status_code == HTTPStatus.OK and
                user.get('email') == user_with_all_data.get('email') and
                user.get('name') == user_with_all_data.get('name')
            ), (
                f'{response.status_code} {response.text}'
            )

    @allure.title('Create a user')
    @allure.description('Create a user with existent data {registered_user}')
    def test_create_user_with_existent_data(self, registered_user):
        response = UserMethod(data.REGISTER_URL).register(
            payload=registered_user
        )
        with allure.step('Checking the body of response {response.text}'):
            assert (
                response.status_code == HTTPStatus.FORBIDDEN and
                response.text == ('{"success":false,'
                                  '"message":"User already exists"}')
            ), (
                f'{response.status_code} {response.text}'
            )

    @allure.title('Create a user')
    @allure.description('Create a user without '
                        'one of required data {wrong_user_data}')
    @pytest.mark.parametrize('wrong_user_data',
                             [data.UserData().without_email,
                              data.UserData().without_password,
                              data.UserData().without_name])
    def test_create_user_without_one_of_required_data(self, wrong_user_data):
        response = UserMethod(data.REGISTER_URL).register(
            payload=wrong_user_data
        )
        with allure.step('Checking the body of response {response.text}'):
            assert (
                response.status_code == HTTPStatus.FORBIDDEN and
                response.text == ('{"success":false,"message":"Email, '
                                  'password and name are required fields"}')
            ), (
                f'{response.status_code} {response.text}'
            )
