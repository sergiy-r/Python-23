# tuples

my_tuple = tuple()  # create an empty tuple
my_tuple1 = ()  # create an empty tuple
print(type(my_tuple), type(my_tuple1))

my_tuple = (1, 2, 3)
print(my_tuple, type(my_tuple))

print('*****')

my_variable = (1)
print(my_variable, type(my_variable))
my_tuple = (1,)
print(my_tuple, type(my_tuple))

print('*****')

my_tuple = tuple(('a', 'b', 'c'))  # notice the use of double brackets, as tuple expects a single argument
print(my_tuple, type(my_tuple))

my_tuple = 'a', 'b', 'c'  # tuple can be created without the use of round brackets
print(my_tuple, type(my_tuple))

first_item = my_tuple[0]  # get first element
print(first_item)
