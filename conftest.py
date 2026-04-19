import pytest

import data
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
def authorized_user_token(registered_user):
    response = UserMethod(data.LOGIN_URL).login(
            payload=data.UserData.data_for_login(registered_user)
    )
   
    return response.json().get('accessToken')
