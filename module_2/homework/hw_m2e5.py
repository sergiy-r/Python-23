# homework module 2 exercise 5

# Напишіть програму на Python, яка підраховує кількість разів, коли заданий символ зустрічається в рядку.
#
# Задачі:
#
# 	1. Використовуючи зазначені змінні message, рядок, у якому буде виконуватися пошук, та search, символ, який ми шукаємо, підрахуйте, скільки разів символ search зустрічається в рядку message.
# 	2. Для підрахунку використовуйте цикл for, який проходить через кожен символ у message.
# 	3. Якщо поточний символ збігається з символом у змінній search, збільште змінну result на 1.
# 	4. Збережіть кінцеву кількість входжень в змінну result.
#
# Очікуваний результат:
#
# Програма має зберегти в змінній result кількість разів, коли символ search зустрічається в рядку message.
#
# Підказки:
#
# 	• Використовуйте == для порівняння поточного символу з символом, який шукаєте.
# Пам'ятайте, що цикл for автоматично проходить через кожен символ у рядку.

message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for char in message:
    if char == search:
        result += 1
print(f"The count of character {search} in the message is {result}.")