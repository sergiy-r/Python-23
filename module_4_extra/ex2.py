"""
У тебе є стіл з усіма наявними товарами в магазині. Дані представлені у вигляді списку словників
Твоя місія - знайти ТОП найдорожчих товарів. Кількість товарів, які ми шукаємо, буде передано у першому аргументі,
а самі дані щодо товарів будуть передані другим аргументом.
Вхідні дані: Число та список словників (int and list of dicts). Кожен словник має 2 ключі "name" та "price".
Вихідні дані: Такий, як і другий аргумент.
Приклади:
"""

def bigger_price(count: int, groceries: list):
    sorted_list = sorted(groceries, key=lambda x: x['price'], reverse=True)
    print(sorted_list)

    return sorted_list[:count]




assert bigger_price(
    2,
    [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1},
    ],
) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
assert bigger_price(
    1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
) == [{"name": "whiteboard", "price": 170}]
