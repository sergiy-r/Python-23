# Create a program that had input two integers k, l.
# If they are not equal, the smaller number is replaced by the greater, otherwise both numbers are replaced by 0.

k = int(input('Enter number k: '))
l = int(input('Enter number l: '))

if k != l  # True
    if k <l:
        k = l
    else:
        l = k
else:
    l = 0
    k = 0

print(k,l)