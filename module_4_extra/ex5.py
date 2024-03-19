"""
У Джо Палуки товсті пальці, тому він завжди натискає клавішу "Caps Lock", коли насправді має намір натиснути клавішу
"a". (Коли Джо намагається ввести якусь акцентовану версію "a", яка потребує більше натискань клавіш для створення
акцентів, він більш обережний у присутності таких рафінованих символів ([Shift] + [a]) і буде натискати клавіші
правильно). Обчисліть і виведіть результат введення Джо заданого тексту. Клавіша "Caps Lock" впливає лише на клавіші
з літерами від "a" до "z", і не впливає на інші клавіші або символи. вважається, що клавіша "Caps Lock" спочатку
вимкнена.
"""

def caps_lock(text:str)->str:
    # text_out = ''
    # up_case = False
    # for char in text:
    #     if char != 'a':
    #         text_out += char.upper() if up_case else char
    #     else:
    #         up_case = not up_case

    split_text = text.split('a')
    for i in range(1, len(split_text), 2):
        split_text[i] = split_text[i].upper()

    print(split_text)

    return ''.join(split_text)




assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"