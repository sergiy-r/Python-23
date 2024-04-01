# Example 1
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function

# Створення замикання
my_func = outer_function("Hello, world!")
print(type(my_func))  # <class 'function'>
my_func()

# Example 2

from typing import Callable

def counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        # використовуємо nonlocal, щоб змінити змінну в замиканні
        nonlocal count
        count += 1
        return count


    return increment

# Створення лічильника
count_calls = counter()

# Виклики лічильника
print(count_calls())  # Виведе 1
print(count_calls())  # Виведе 2
print(count_calls())  # Виведе 3
