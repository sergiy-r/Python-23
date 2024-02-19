# operation on lists

some_list = ["a", "b", "c"]
first_letter = some_list[0]  # assign first element in the list
middle_one = some_list[1]
last_letter = some_list[2]
print(first_letter, middle_one, last_letter)

# print list elements using reverse index reference
print(some_list[-1], some_list[-2], some_list[-3])


removed_char = some_list.pop(1)
print(removed_char)

some_list.append('z')
print(some_list)

some_list.remove('z')
print(some_list)

some_list.insert(1, 'b')
print(some_list)

another_list = [1,2]
some_list.extend(another_list)
print(some_list)

some_list.remove(1)
print(some_list)

some_list.remove(2)
print(some_list)

some_list_copy1 = some_list.copy()  # Copy list using list.copy() method
some_list_copy2 = list(some_list)  # Copy list using list constructor method
some_list_copy3 = some_list[:]  # Copy list using list slicing method

print(f'Original list: {some_list}')

some_list.clear()  # Clear the list

print(f'Cleared list: {some_list}')
print(f'List copy using list.copy() method: {some_list_copy1}')
print(f'List copy using list constructor method list(): {some_list_copy2}')
print(f'List copy using slicing method new_list = old_list[:]: {some_list_copy3}')


