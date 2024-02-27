# Find index of first occurrence of 'a' in a string

s = input('Enter a string: ')
index = 0  # set this to -1 instead of 0 in case 'a' is not found in the input string

for char in s:
    print(f'char: {char}')
    if char == 'a':
        break  # break will be applied only if symbol is 'a'
    index += 1
print(f"First occurrence of 'a' is at index {index}")

# a can also be found using .index('a')
