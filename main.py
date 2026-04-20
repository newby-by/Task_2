# import data
# from methods.ingredient import IngredientMethod


# _data = IngredientMethod(url=data.INGREDIENT_URL).get_ingredients()
# print(_data)


from data import OrderData

order = OrderData()

print(len(order._data))

print("bun", len(order._buns))
print(order._buns)
print("sauce", len(order._sauce))
print(order._sauce)
print("main", len(order._main))
print(order._main)
print("unknown", len(order._unknown))
print(order._unknown)
