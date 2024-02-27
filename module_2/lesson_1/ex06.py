# optimised version of ex05

operator = '+'
res = (operator, 5, 5)
match res:
    case ('+' | '-' | '*',  x, y):
        print(eval(f'{x} {operator} {y}'))
    case ('/', x, 0):
        print("Can't divide by 0")
    case ("/", x, y):
        print(x / y)
    case _:
        print('Unknown operator')