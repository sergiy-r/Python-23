# if statement

number = int(input('Enter a number: '))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


# elif

number = int(input('Enter a number: '))

if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is an negative number.")
else:
    print(f"{number} is obviously a zero.")

# implicit type change to bool

money = 0  # 0 is False
if money:
    print(f"You have {money} in your bank account")
else:
    print("You have no money  in your account")

result = None  # None is False
if result:
    print(result)
else:
    print("Result is None, do something")

user_name = input("Enter your name: ")

if user_name:  # Empty string is False
    print(f"Hello {user_name}")
else:
    print("Hi Anonymous!")

# any values other than 0, None or empty string/object returns True
# is operator checks if two objects refer to the same area in memory, i.e., that they are the same object
# it is different to == operator that check whether the values of two objects are the same

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(f"\n")
print ('a:', a, ', b = a', ', c:', c)
print('a is b', a is b)  # True
print('a is c', a is c)  # False
print('a == b', a == b)  # True
print('a == c', a == c)  # False

# boolean algebra

num = int(input("Enter number: "))
length = len(str(num))
if length == 2 and num % 2 == 0:
    print("This is a two digit even number")
else:
    print("This is not a two digit even number")

a = True and False  # False
a = True or False  # True
a = not 2 < 0  # True





