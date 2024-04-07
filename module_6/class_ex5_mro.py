# Example of Method Resolution Order in Python

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())  # Виведе порядок розв'язання методів для класу D


class AA:
    name = "Я клас AA"

class BB:
    name = "Я клас BB"
    property = "Я знаходжусь в класі BB"

class CC(AA, BB):
    property = "Я знаходжусь в класі C"

c = CC()
print(f"c.name: {c.name}")
print(f"c.property: {c.property}")
