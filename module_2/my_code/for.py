fruit = 'apple'
for char in fruit:
    print(char)

alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")
print(' \n')


for i in range(1, 10):
    if i % 2 == 0:
        print(f"{i} є парним числом.")
    else:
        print(f"{i} є непарним числом.")
