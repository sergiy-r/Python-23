# tuple
empty_tuple = ()

empty_tuple = tuple()

languages = 'Python', 'C', 'Java'  # create
print(languages, type(languages))

p = languages[0]
print(p)

p, c, c_ = languages  # tuple unpacking, number of variables needs to correspond to the number of elements in

p, c, *_ = languages  # if you need to assign only the first two elements, then you need to assign all remaining\
# elements to the third variable starting with '*', e.g., '*_'