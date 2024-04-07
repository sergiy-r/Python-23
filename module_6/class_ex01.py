class User:
    name = 'Anonymous'
    age = 15

user1 = User()
print(user1.name)
print(user1.age)

user2 = User()
user2.name = "John"
# user2.age = 90

print(user2.name)
print(user2.age)

print('*' * 24)

class MyClass:
    def __init__(self, value):
        self.instance_field = value  # Поле класу

obj1 = MyClass(5)
obj2 = MyClass(10)
print(obj1.instance_field)

print('*' * 24)


class Person:
    hobby = 'football'
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_name(self) -> None:
        print(f'Hi! I am {self.name} and I am {self.age} years old.')

    def set_age(self, age: int) -> None:
        self.age = age

bob = Person('Boris', 34)
rob = Person('Rob',25)
print(rob.name, rob.age)

bob.say_name()
bob.set_age(25)
bob.say_name()
rob.say_name()
rob.set_age(30)
rob.say_name()
rob.hobby = 'games'
print(rob.hobby)
Person.hobby = 'pool'
print(bob.hobby, rob.hobby)
