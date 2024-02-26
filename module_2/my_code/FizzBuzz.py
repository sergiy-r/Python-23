#  Виводить "Fizz", якщо число кратне якомусь певному числу (наприклад, 3);
#  Виводить "Buzz", якщо число кратне іншому певному числу (наприклад, 5);
#  Виводить "FizzBuzz", якщо число кратне обом цим числам;
#  В іншому випадку виводить саме число.

num = int(input('Enter a number to be evaluated: '))
factor_1 = 2
factor_2 = 3
print(f"Factor 1: {factor_1}")
print(f"Factor 2: {factor_2}")

fizz = num % factor_1 == 0
buzz = num % factor_2 == 0

if fizz and buzz:
    print(f"FizzBuzz - both {factor_1} and {factor_2} are factors of {num}")
elif fizz:
    print(f"Fizz - only {factor_1} is a factor of {num}")
elif buzz:
    print(f"Buzz - only {factor_2} is a factor of {num}")
else:
    print(f"{num} - neither {factor_1} nor {factor_2} are factors of {num}")