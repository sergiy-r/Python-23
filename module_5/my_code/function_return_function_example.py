from typing import Callable

def power(exponent: int) -> Callable[[int], int]:
    def inner(some_number: int) -> int:
        return some_number ** exponent
    return inner

# Використання
square = power(2)
cube = power(3)

print(square(4))
print(cube(4))
