import json

import pytest

import data
from methods.order import OrderMethod
from methods.user import UserMethod


@pytest.fixture(scope='function')
def user():
    return data.UserData()


@pytest.fixture(scope='function')
def user_with_all_data(user):
    return user.with_all_data


@pytest.fixture(scope='function')
def registered_user(user_with_all_data):
    UserMethod(data.REGISTER_URL).register(
            payload=user_with_all_data
    )
    return user_with_all_data


@pytest.fixture(scope='function')
def empty_token():
    return ''


@pytest.fixture(scope='function')
def authorized_user_token(registered_user):
    response = UserMethod(data.LOGIN_URL).login(
            payload=data.UserData.data_for_login(registered_user)
    )

    return response.json().get('accessToken')


@pytest.fixture(scope='function')
def registered_user_with_1_order_token(authorized_user_token):
    headers = {
            'Authorization': authorized_user_token,
            'Content-Type': 'application/json'
        }
    OrderMethod(url=data.ORDER_URL).order(
        payload=json.dumps(data.OrderData().buns_only),
        headers=headers
    )

    return authorized_user_token


@pytest.fixture(scope='function')
def registered_user_with_2_orders_token(registered_user_with_1_order_token):
    headers = {
            'Authorization': registered_user_with_1_order_token,
            'Content-Type': 'application/json'
        }
    OrderMethod(url=data.ORDER_URL).order(
        payload=json.dumps(data.OrderData().buns_and_sauce),
        headers=headers
    )

    return registered_user_with_1_order_token
