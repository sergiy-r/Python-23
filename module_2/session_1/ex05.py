# match case

# res = ('/', 5, 2)
#
# match res:
#     case ('+', x, y):
#         print(x + y)
#     case ('-', x, y):
#         print(x - y)
#     case ('*', x, y):
#         print(x + y)
#     case ('/', x, 0):
#         print("Can't divide by 0")
#     case ('/', x, y):
#         print(x / y)
#     case _:
#         print('Unknown operator')

# optimised version

operator = '+'
res = (operator, 5, 5 )
match res:
    case ('+' | '-' | '*',  x, y):
        if operator = '+':
            print(x+y)
        elif operator == '-':
            print(x-y)
        else:
            print(x*y)
    case ('/', x, 0):
        print("Can't divide by 0")
    case ('/', x, y):
        print(x / y)
    case _:
        print('Unknown operator')