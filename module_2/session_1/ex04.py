# Find index of the last occurrence of 'a' in a string

s = input('Enter a string: ')
index = -1  # set this to -1 instead of 0 in case 'a' is not found in the input string
count = 0
for char in s:
    if char == 'a':
        index = count
    count += 1

print(index)


#print(f"First occurrence of 'a' is at index {index}")

# a can also be found using .index('a')
