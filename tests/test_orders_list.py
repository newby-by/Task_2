from http import HTTPStatus

import allure
import pytest

import data
from methods.order import OrderMethod


@allure.feature('Test for getting a list of orders')
class TestOrderList:

    @allure.title('Get a list of orders')
    @allure.description('Auth user has not had any orders')
    def test_get_list_of_orders_auth_user_no_orders(
        self, authorized_user_token
    ):
        headers = {
            'Authorization': authorized_user_token,
            'Content-Type': 'application/json'
        }
        response = OrderMethod(url=data.ORDER_URL).orders_list(
            headers=headers
        )

        assert (response.status_code == HTTPStatus.OK and
                len(response.json().get('orders')) == 0)

    @allure.title('Get a list of orders')
    @allure.description('Auth user has some orders')
    @pytest.mark.parametrize(
        'fixture,expected', [
            ('registered_user_with_1_order_token', 1),
            ('registered_user_with_2_orders_token', 2),
        ]
    )
    def test_get_list_of_orders_auth_user_with_some_orders(
        self, fixture, expected, request
    ):
        headers = {
            'Authorization': request.getfixturevalue(fixture),
            'Content-Type': 'application/json'
        }
        response = OrderMethod(url=data.ORDER_URL).orders_list(
            headers=headers
        )

        assert (response.status_code == HTTPStatus.OK and
                len(response.json().get('orders')) == expected)

    @allure.title('Get a list of orders')
    @allure.description('With guest user')
    def test_get_list_of_orders_by_guest_user(self):
        response = OrderMethod(url=data.ORDER_URL).orders_list()

        assert (response.status_code == HTTPStatus.UNAUTHORIZED and
                response.text == ('{"success":false,"message":'
                                  '"You should be authorised"}'))

    @allure.title('Get a list of all orders')
    @allure.description('With auth user and quest user')
    @pytest.mark.parametrize('fixture',
                             ['authorized_user_token',
                              'empty_token'])
    def test_get_list_of_all_orders_auth_user(self, fixture, request):
        headers = {
            'Authorization': request.getfixturevalue(fixture),
        }
        response = OrderMethod(url=data.ALL_ORDERS_URL).orders_list(
            headers=headers
        )

        assert (response.status_code == HTTPStatus.OK and
                len(response.json().get('orders')) ==
                data.MAX_NUMBER_OD_ORDER_IN_LIST)
