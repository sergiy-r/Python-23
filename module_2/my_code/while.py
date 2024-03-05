# a = 0
# while a < 6:
#     a = a + 1
# #    print(f"'a = {a}, remainder (div by 2) = {a % 2}")
#     if not a % 2:
#         continue
#     print(f"a % 2 = {a % 2}")
#     print(a)


while True:
    number = input("number = ")
    number = int(number)
    if number < 0:
        break
    while True:
        print(number)
        number = number - 1
        if number < 0:
            break

