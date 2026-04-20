import allure

from methods.base_method import BaseMethod


@allure.title('The methods for order objects')
class OrderMethod(BaseMethod):

    @allure.step('Order a burger')
    def order(self, *, payload=None, headers=None):
        response = self.post(
            payload=payload,
            headers=headers
        )

        return response
    
    @allure.step('Get a list of orders')
    def orders_list(self, *, headers=None):
        response = self.get(
            headers=headers
        )

        return response
    
    @staticmethod
    def get_ids(response):
        _data = response.json().get('order').get('ingredients')
        return [el.get('_id') for el in _data]
