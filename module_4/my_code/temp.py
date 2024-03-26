
from pprint import pprint
squares = [x**2 for x in range(10)]
list_of_squares = [(num, num**2) for num in range(0, 11)]
pprint(list_of_squares)