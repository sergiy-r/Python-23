"""
Як із рядка слов отримати словник де ключи та значення записані попарно.
Наприклад: "Hello Hi Bye Goodbye List Array"
{"Hello": "Hi",
"Bye": "Goodbye",
"List": "Array"}
"""

string = "Hello Hi Bye Goodbye List Array"
list_str = string.split()
my_dict = {}
for i in range(0, len(list_str), 2):
    my_dict[list_str[i]] = list_str[i+1]
    my_dict[list_str[i+1]] = list_str[i]
print(my_dict)