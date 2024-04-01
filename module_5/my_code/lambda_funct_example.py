# Bad labmda example
# Syntax: lambda arguments: expression

add = lambda x, y: x + y
print(add(5, 3))  # Виведе 8

# lambda functions shouldn't be stored in variables and only defined in the place where they are used, as below

print((lambda x, y: x + y)(5, 3))  # Виведе 8

# Лямбда-функції не мають імені. Зазвичай використовуються для написання коротких функцій. Можуть містити тільки один
# вираз і не можуть містити блоки команд наприклад, цикли або умовні конструкції.

