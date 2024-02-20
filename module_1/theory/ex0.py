# mutable and immutable
a = 'Hello'
print(a, id(a))

a = a.upper()
print(a, id(a))  # memory IDs are different, so strings are immutable
