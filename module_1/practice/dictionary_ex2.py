# dictionary update
first = {'a': 10, 'b': 20}
second = {'b': 'other'}
print(first)

first.update(second)  # copies elemnts from second to first and updates any values in the first
print(first)

# N.B. keys in dictionary must be unique