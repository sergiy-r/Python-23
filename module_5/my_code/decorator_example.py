# Decorators Example 1

# a complicated approach
def complicated(x: int, y: int) -> int:
    return x + y

def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

complicated = logger(complicated)
print(complicated(2, 3))

"""
Проте такий код не занадто легкий для читання і досить об'ємний. Крім того, в коді легко пропустити рядок 
complicated = logger(complicated) і не занадто просто зрозуміти, звідки виходитиме доданий до complicated функціонал.
Щоб спростити застосування цього шаблону проектування, в Python є спеціальний синтаксис декоратора. Декоратори 
використовуються з синтаксисом @, що робить їх застосування простим та елегантним. Точно той самий код, який робить 
абсолютно те саме, можна записати у вигляді:
"""

def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x + y

print(complicated(2, 3))
