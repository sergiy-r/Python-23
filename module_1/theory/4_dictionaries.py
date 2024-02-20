# dictionary methods

my_dict = {"name": "Alice", "age": 25}  # create a dictionary
print(my_dict)

my_dict.update({"email": "alice@example.com", "age": 26})   # update a dictionary
print(my_dict)

new_dict = my_dict.copy()
print(new_dict)

age = my_dict.get("age")  # Поверне 25
gender = my_dict.get("gender")  # Поверне None, оскільки "gender" немає в словнику
print(age, gender)

name = my_dict["name"]  # Поверне 'Alice'
print(name)
# gender = my_dict["gender"]  # Викличе KeyError, оскільки "gender" немає в словнику
