# Variable type transformation
a = '56'
c = 45
print(type(a))
b = int(a)  # to integer
res = c + b
print(type(b))
print(res)
res_1 = str(res)  # to string

s = '56.5'
t = int(float(s))  # if a number has a decimal separator transform to float first, then to string
