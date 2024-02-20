# dictionary methods

my_dict = {"name": "Alice", "age": 25}  # create a dictionary
print(my_dict)

age = my_dict.pop("age")  # remove key value pair age and assign to age variable
print(age)
print(my_dict, '-after removing age')

my_dict.update({"email": "alice@example.com", "age": 26})   # update a dictionary
print(my_dict)

new_dict = my_dict.copy()
print(new_dict, '- new dictionary')

age = my_dict.get("age")  # Поверне 25
gender = my_dict.get("gender")  # Поверне None, оскільки "gender" немає в словнику
print(age, gender)

name = my_dict["name"]  # Поверне 'Alice'
print(name)
# gender = my_dict["gender"]  # Викличе KeyError, оскільки "gender" немає в словнику


# Створіть програму на Python, яка ініціалізує порожній словник і заповнює його певними ключами та відповідними значеннями.

# Задачі:
# Створіть порожній словник data.
# Додайте до словника data наступні пари ключ-значення:
# Ключ year зі значенням цілого числа 2024.
# Ключ lang зі значенням рядка 'Python'.
# Ключ version зі значенням дійсного числа 3.12.
# Очікуваний результат:
#
# Після виконання програми, словник data повинен містити три пари ключ-значення, як вказано вище.

data = {}
data.update({'year':2024, 'lang':'Python', 'version':3.12})
print(data)

# Задачі:
#
# Використовуйте словник cat для зберігання інформації про кота. Додайте до нього наступні ключі та відповідні значення:
# Ключ "nick" з рядковим значенням імені кота (наприклад, "Simon").
# Ключ "age" з цілим числовим значенням віку кота (наприклад, 7).
# Ключ "characteristics" зі списком характеристик кота (наприклад, ["лагідний", "кусається"]).
# Оголосіть змінну age та використовуйте метод get для отримання віку кота зі словника cat.
# Використайте метод update, щоб додати до словника cat всі пари ключ-значення зі словника info.
# Очікуваний результат:
# Після виконання програми, словник cat повинен містити всю вказану інформацію про кота, включаючи ім'я, вік, характеристики та додаткові дані зі словника info.

print('*****')
cat = {}
info = {"status": "vaccinated", "breed": True}
cat.update({'nick':'Simon', 'age':7, 'characteristics': ["лагідний", "кусається"]})
age = cat.get('age')
cat.update(info)
print(cat)