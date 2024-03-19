fh = open('test.txt', 'w+')
fh.write('hello!')
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)  # 'he'

fh.close()

# read one character at a time from file
fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)

fh.close()

# read one line from file at a time

fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()

# strip the end of the line
fh = open("test.txt", "w")
fh.write("first line\nsecond line\nthird line")
fh.close()

fh = open("test.txt", "r")
lines = [el.strip() for el in fh.readlines()]
print(lines)

fh.close()
