from methods.base_method import BaseMethod


class IngredientMethod(BaseMethod):

    def get_ingredients(self, headers=None) -> list:
        response = self.get(
            headers=headers
        )
        return response.json().get('data')
