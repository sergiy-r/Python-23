# Temp File
#
# some_iterable = ["a", "b", "c"]
# some_iterable[2] = 'z'
# print(some_iterable)

my_list = list()
print(type(my_list), 'list')
my_list = [1, 2, 3, 4, 5]
print(type(my_list), 'list')

my_dict = dict()
print(type(my_dict), 'dict')
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(type(my_dict), 'dict')

my_set = set()
print(type(my_set), 'set')
my_set = {1, 2, 3}
print(type(my_set), 'set')

my_frozenset = frozenset()
print(type(my_frozenset), 'frozen set')
my_frozenset = frozenset([1, 2, 3])
print(type(my_frozenset), 'frozen set')
