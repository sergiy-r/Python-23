# sets
a = {1, 3, 5, 66}
print(a)
print(type(a))

l = ['Test', 55]
l_set = frozenset(l)
print(l_set)

#a.add(l_set)
print(a)
# sets are unsorted and immutable
# sets hold only unique elements

a.union(l)
print(a)
languages = ['C', 'C++', 'Java', 'Python', 'Java', 'C']
print(languages)
languages_set = set(languages)
print(languages_set)
languages = list(languages_set)
print(languages)

