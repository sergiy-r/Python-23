# swap

baz = int(input('Enter a number baz: '))
foo = int(input('Enter a number foo: '))

# if baz < foo:
#     temp.txt = baz
#     baz = (baz + foo) / 2
#     foo = temp.txt * foo
#
# else:
#     temp.txt = foo
#     foo = (foo +baz) / 2
#     baz = temp.txt * baz

if baz < foo:
    baz, foo = (baz + foo) / 2, baz * foo
else:
    foo, baz = (foo + baz) / 2, baz * foo

print(baz, foo)

a = 5
b = 3

print(a, b)

a, b = b, a

print(a, b)
