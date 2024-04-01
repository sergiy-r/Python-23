# List comprehensions examples
# syntax: [new_item for item in iterable if condition]

# Example 1
sq = [x**2 for x in range(1, 6)]
print(sq)

# Example 2 with condition
even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
print(even_squares)

# equivalent conde without comprehension
even_squares = []
for x in range(1, 10):
    if x % 2 == 0:
        even_squares.append(x**2)

print(even_squares)  # Виведе [4, 16, 36, 64]


# Set comprehension
# Syntax: {new_item for item in iterable if condition}

odd_squares = {x**2 for x in range(1, 10) if x % 2 != 0}
print(odd_squares)

# Dictionary comprehension
# Syntax: {key: value for item in iterable if condition}

# Example 1
sq = {x: x**2 for x in range(1, 10)}
print(sq)

# Example 2 with condition
sq_dict = {x: x**2 for x in range(1, 10) if x > 5}
print(sq_dict)



