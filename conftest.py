import pytest

import data


@pytest.fixture(scope='function')
def user():
    return data.UserData()


@pytest.fixture(scope='function')
def user_with_all_data():
    return data.UserData().with_all_data
