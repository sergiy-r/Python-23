# iterate through dictionary in for

numbers = {
    1: "one",
    2: "two",
    3: "three"
}
for key in numbers:
    print(key)

print(' \n')

# the same output can be achieved using 'key' method
for key in numbers.keys():
    print(key)

print(' \n')

# use 'values' method to return values from dictionary
for val in numbers.values():
    print(val)

print(' \n')

# use 'items' method to iterate through pairs (key, value)
for key, value in numbers.items():
    print(key, value)
