import json
from http import HTTPStatus

import allure
import pytest
import requests

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

    @allure.title('Login a user')
    @allure.description('Login a user with existent data {registered_user}')
    def test_login_existent_user(self, registered_user):
        response = UserMethod(data.LOGIN_URL).login(
            payload=data.UserData.data_for_login(registered_user)
        )
        actual_user_data = response.json().get('user')
        with allure.step('Checking the body of response {response.text}'):
            assert (
                response.status_code == HTTPStatus.OK
                and
                actual_user_data.get('email') == registered_user.get('email')
                and
                actual_user_data.get('name') == registered_user.get('name')
            ), (
                f'{response.status_code} {response.text}'
            )

    @allure.title('Login a user')
    @allure.description('Login a user with wrong data user: email or password {registered_user}')
    @pytest.mark.parametrize('method', [data.UserData.change_email, data.UserData.change_password])
    def test_login_with_wrong_data_user(self, method, registered_user):
        response = UserMethod(data.LOGIN_URL).login(
            payload=method(data.UserData.data_for_login(registered_user))
        )
        with allure.step('Checking the body of response {response.text}'):
            assert (
                response.status_code == HTTPStatus.UNAUTHORIZED and
                response.text == '{"success":false,"message":"email or password are incorrect"}'
            ), (
                f'{response.status_code} {response.text}'
            )

    @allure.title('Change a user data')
    @allure.description('Change a user data by authorized user')
    def test_change_user_data_by_auth_user(self, authorized_user_token):
        headers = {
            'Authorization': authorized_user_token,
            'Content-Type': 'application/json'
        }
        new_user_data = data.UserData().without_password
        response = UserMethod(data.USER_URL).change_data(
            payload=json.dumps(new_user_data),
            headers=headers
        )
        MESSAGE = ('{"success":true,"user":'
                   '{"email":"' + f'{new_user_data.get('email')}",'
                   '"name":"' + f'{new_user_data.get('name')}"' + '}}')
        with allure.step('Checking the body of response {response.text}'):
            assert (
                response.status_code == HTTPStatus.OK and
                response.text == MESSAGE
            ), (
                f'{response.status_code} {response.text}'
            )

    @allure.title('Change a user data')
    @allure.description('Change a user data by guest')
    def test_change_user_data_by_guest(self):
        new_user_data = data.UserData().without_password
        response = UserMethod(data.USER_URL).change_data(
            payload=json.dumps(new_user_data)
        )
       
        with allure.step('Checking the body of response {response.text}'):
            assert (
                response.status_code == HTTPStatus.UNAUTHORIZED and
                response.text == '{"success":false,"message":"You should be authorised"}'
            ), (
                f'{response.status_code} {response.text}'
            )
