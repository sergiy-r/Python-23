# dictionary get

first = {'a':10, 'b': 20, 'c': 30, 'd': 40}

print(first['a'])
print(first['d'])
print(first.get('a'))

first['a'] = 'asdfasdf'
print(first['a'])
print(first.keys())
print(list(first.keys()))

print(first.values())
print(first.items())
