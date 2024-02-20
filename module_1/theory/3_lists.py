# list methods and operations on lists

some_list = ["a", "b", "c"]
first_letter = some_list[0]  # assign first element in the list
middle_one = some_list[1]
last_letter = some_list[2]
print(first_letter, middle_one, last_letter)

# print list elements using reverse index reference
print(some_list[-1], some_list[-2], some_list[-3])


removed_char = some_list.pop(1)  # remove an element (object) using index
print(removed_char)

some_list.append('z')
print(some_list)

some_list.remove('z')  # remove a value (object) from list
print(some_list)

some_list.insert(1, 'b')  # insert an element (object) into list at index position
print(some_list)

another_list = [1, 2]
some_list.extend(another_list)  # extend list 1 using another list
print(some_list)

some_list.remove(1)  # remove element with index 1
print(some_list)

some_list.remove(2)
print(some_list)

some_list_copy1 = some_list.copy()  # Create a copy of the list using list.copy() method
some_list_copy2 = list(some_list)  # Create a copy of the list using list constructor method
some_list_copy3 = some_list[:]  # Create a copy of the list using list slicing method

print(f'Original list: {some_list}')

some_list.clear()  # Clear the list

print(f'Cleared list: {some_list}')
print(f'List copy using list.copy() method: {some_list_copy1}')
print(f'List copy using list constructor method list(): {some_list_copy2}')
print(f'List copy using slicing method new_list = old_list[:]: {some_list_copy3}')

new_list1 = list((some_list_copy1, some_list_copy2))
print(new_list1)

new_list2 = [*some_list_copy1, *some_list_copy2]  # create a new list using the * operator (list unpacking)
print(new_list2, ' - list unpacking method using * operator')

new_list3 = some_list_copy1 + some_list_copy2  # create a new list using the + operator (concatenation)
print(new_list2, ' - concatenation of two lists using + operator')

new_list2.index('b')
new_list2.count('a')  # count number of occurrences of an object in a list
print(f"Letter 'a' is found {new_list2.count('a')} times in new_list2\
      \nand first instance of letter 'b' is at index {new_list2.index('b')}")

words = ["banana", "apple", "cherry"]
words.sort(key=len, reverse=True)  # sort by length in reverse order
print(words)  # Виведе ['apple', 'banana', 'cherry']

