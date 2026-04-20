import json
from http import HTTPStatus

import allure
import pytest

import data
from methods.order import OrderMethod


@allure.feature('Tests for methods of order objects')
class TestOrder:

    @allure.title('Order a burger')
    @allure.description('with auth user and order data {order_data}')
    @pytest.mark.parametrize(
        'order_data',
        [data.OrderData().buns_only, data.OrderData().buns_and_sauce])
    def test_create_order_auth_user(self, order_data, authorized_user_token):
        headers = {
            'Authorization': authorized_user_token,
            'Content-Type': 'application/json'
        }
        response = OrderMethod(url=data.ORDER_URL).order(
            payload=json.dumps(order_data),
            headers=headers
        )

        assert (response.status_code == HTTPStatus.OK and
                len(order_data.get('ingredients')) ==
                len(OrderMethod.get_ids(response))) 

    @allure.title('Order a burger')
    @allure.description('with auth user and without ingredients')
    def test_create_order_auth_user_without_ingredients(
        self, authorized_user_token
    ):
        headers = {
            'Authorization': authorized_user_token,
            'Content-Type': 'application/json'
        }
        response = OrderMethod(url=data.ORDER_URL).order(
            payload=json.dumps(data.OrderData().empty_order),
            headers=headers
        )

        assert (response.status_code == HTTPStatus.BAD_REQUEST and
                response.text == ('{"success":false,"message":'
                                  '"Ingredient ids must be provided"}'))

    @allure.title('Order a burger')
    @allure.description('with auth user and with wrong id of an ingredient')
    def test_create_order_auth_user_with_wrong_id_ingredient(
        self, authorized_user_token
    ):
        headers = {
            'Authorization': authorized_user_token,
            'Content-Type': 'application/json'
        }
        response = OrderMethod(url=data.ORDER_URL).order(
            payload=json.dumps(data.OrderData().wrong_id),
            headers=headers
        )

        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    
    @allure.title('Order a burger')
    @allure.description('with guest and order data {order_data}')
    @pytest.mark.parametrize(
        'order_data',
        [data.OrderData().buns_only, data.OrderData().buns_and_sauce])
    def test_create_order_by_guest_user_with_order_data(self, order_data):
        response = OrderMethod(url=data.ORDER_URL).order(
            payload=json.dumps(order_data),
        )

        assert (response.status_code == HTTPStatus.BAD_REQUEST and
                response.text == ('{"success":false,"message":'
                                  '"Ingredient ids must be provided"}'))
    
    @allure.title('Order a burger')
    @allure.description('with guest user and without ingredients')
    def test_create_order_by_guest_user_without_ingredients(self):
        response = OrderMethod(url=data.ORDER_URL).order(
            payload=json.dumps(data.OrderData().empty_order)
        )

        assert (response.status_code == HTTPStatus.BAD_REQUEST and
                response.text == ('{"success":false,"message":'
                                  '"Ingredient ids must be provided"}'))

    @allure.title('Order a burger')
    @allure.description('with guest user and with wrong id of an ingredient')
    def test_create_order_by_guest_user_with_wrong_id_ingredient(self):
        response = OrderMethod(url=data.ORDER_URL).order(
            payload=json.dumps(data.OrderData().wrong_id)
        )

        assert (response.status_code == HTTPStatus.BAD_REQUEST and
                response.text == ('{"success":false,"message":'
                                  '"Ingredient ids must be provided"}'))
