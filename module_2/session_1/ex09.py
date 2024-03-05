# Identify how many students with higher than average points
# User enters number of students, names and points for each.
# Program identifies average and names of students with points above average

students = {}  # dictionary
count = int(input('How many students: '))
s = 0
for i in range(count):
    name = input('Please enter name: ')
    point = int(input('Please enter point: '))
    students[name] = point # {'Anna': 5, 'Andrew': 4}
    sum += point  # sum = sum + point
avg = sum / count
print(f'The averate point is {avg}. Students with average point is: ')
for student in students:
    if students[student] > avg:
        print (student)

