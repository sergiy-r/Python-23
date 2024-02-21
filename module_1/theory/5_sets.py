# Sets
empty_set = set()
print(empty_set)

a = set('Hello')  # create set a using set()
b = {1, 2, 3, 4, 5}  # create set b using {}
print('-----')

# removing duplicates
lst = [1, 2, 3, 1, 2, 2, 3, 4, 1]
print(lst, 'list with duplicates')
d_lst = set(lst)  # convert list lst to set d_lst
lst = list(d_lst)
print(lst, 'list without duplicates')
print('-----')
# adding an element to a set
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # {1, 2, 3, 4}
print('-----')

# remove an element from a list
numbers = {1, 2, 3}
numbers.remove(3)
print(numbers)  # {1, 2}
print('-----')

# Remove element using discard
numbers = {1, 2, 3}
numbers.discard(2)
print(numbers)  # {1, 3}
print('-----')

# Remove element using discard - no value error if element is missing
numbers = {1, 2, 3}
numbers.discard(5)
print(numbers)  # {1, 3}
print('-----')

# to find elements in both sets use '&' operation or intersection() method
a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b), 'intersection() method')  # {3}
print(a & b, "'&' method")  # {3}
print('-----')

# find difference between set a and set b
print(a.difference(b), 'difference using difference() operator')  # {1, 2}
print(a - b)  # {1, 2}
print('-----')

# symmetric difference - find elements from both sets except for common
print(a.symmetric_difference(b), 'symmetric difference')  # {1, 2, 4, 5}
print(a ^ b, "symmetric difference using '^'")  # {1, 2, 4, 5}
print('-----')

# to join (union) two sets, use '|' or union() method
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}
print('-----')

# frozen sets - the set in immutable, i.e. it cannot be changed, but you can stil
union = a | b  # Об'єднання множин
intersection = a & b  # Перетин множин
difference = a - b  # Різниця множин
symmetric_difference = a ^ b  # Симетрична різниця
# the above statements will result in a new frozen set being created

print(union)  # frozenset({1, 2, 3, 4, 5})
print(intersection)  # frozenset({3})
print(difference)  # frozenset({1, 2})
print(symmetric_difference)  # frozenset({1, 2, 4, 5})
