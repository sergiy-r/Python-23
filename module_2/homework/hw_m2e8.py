# homework module 2 exercise 8

# Напишіть програму на Python, яка включає функцію invite_to_event. Ця функція приймає ім'я користувача та повертає персоналізоване запрошення.
#
# Задачі:
#
# 	1. Створіть функцію invite_to_event, яка приймає один параметр - username.
# 	2. Усередині функції використовуйте f-рядок для створення повідомлення з персоналізованим ім'ям.
# 	3. Функція повинна повертати рядок: "Dear {username}, we have the honour to invite you to our event".
#
# Очікуваний результат:
#
# Функція повертає рядок з персоналізованим запрошенням.
#
# Підказки:
#
# Використовуйте return для повернення результату виклику функції invite_to_event.
# Пам'ятайте про використання фігурних дужок {} у f-рядку для вставки значення змінної.

def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event"


print(invite_to_event('Sergiy'))
