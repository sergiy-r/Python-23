# check if the number is a поліндром, e.x.,12321

num = input('Please enter a number or text:')
#print(num[::-1] == num)  #works for numbers, not sure about strings
is_poly = num == num[::-1]
print(is_poly)

# check tutor's longer solution

