# Calculate the area and hypotenuse of a triangle given the sides are known

side1 = float(input('Enter the first side of the triangle: '))
side2 = float(input('Enter the second side of the triangle: '))

hypotenuse = (side1 ** 2 + side2 ** 2) ** 0.5
area = side1 * side2 / 2

print(f'The hypotenuse is {hypotenuse}')
print(f'The area is {area}')

print(f'{side1} + {side2} = {side1 + side2}')