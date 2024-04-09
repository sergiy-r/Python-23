# Exercise 3
"""
Для попереднього завдання реалізуйте в класі Animal метод change_weight, який має змінювати вагу тварини.
Викличте функцію change_weight(12) для об'єкта animal та змініть значення початкової ваги з 10 на 12 одиниць.
"""
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

animal = Animal("Simon", 10)
animal.change_weight(12)


# Exercise 2
"""
Додамо в клас Animal змінну класу color, значення якої спочатку дорівнює 'white', і метод change_color, який 
повинен змінювати значення змінної класу color.
Створіть екземпляри об'єкта: first_animal та second_animal
Викличте функцію change_color("red") для будь-якого екземпляра об'єкту Animal та змініть значення змінної класу color на "red".
"""

class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight


    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, new_color):
        Animal.color = new_color


first_animal = Animal('Cat', 5)
second_animal = Animal('Dog', 10)
print(f"{first_animal.nickname}: {first_animal.color}")
print(f"{second_animal.nickname}: {second_animal.color}")

first_animal.change_color('red') # option 1 to change class attribute by triggering a change for an object
print(f"{first_animal.nickname}: {first_animal.color}")
print(f"{second_animal.nickname}: {second_animal.color}")

Animal.color = 'blue'  # option 2 for changing the class attribute directly
print(f"{first_animal.nickname}: {first_animal.color}")
print(f"{second_animal.nickname}: {second_animal.color}")


# Exercise 5

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


cat = Cat('Simon', 10)
print(cat.say())

# Exercise 6

"""
Створіть клас Dog, батьківським класом якого є клас Animal. У класі Dog виконайте перевизначення методу say, щоб він 
повертав рядок "Woof" для екземплярів класу Dog.

У конструкторі класу Dog введіть нову властивість breed - порода, при цьому повинні залишитись всі властивості, 
успадковані від класу Animal.

Створіть у коді наступний екземпляр класу Dog:
dog = Dog("Barbos", 23, "labrador")
"""

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed

    def say(self):
        return "Woof"

dog = Dog("Barbos", 23, "labrador")
print(dog.nickname, dog.breed, dog.weight, dog.say())


# Exercise 7 Example

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Cat(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Meow"


owner = Owner("Sherlock", 24, "London, 221B Baker Street")
cat = Cat("Simon", 10, "british", owner)
print("\n", "*" * 15, " ", "Exercise 7 Example", " ", "*" * 15, "\n")
print(owner.name, owner.age, owner.address)
print(cat.nickname, cat.weight, cat.breed, cat.owner.name, cat.owner.address)


# Exercise 7
"""
Для минулого завдання додамо клас Owner — власника собаки. У класу є три атрибути: ім'я — name, вік — age та адреса — 
address. Також необхідно реалізувати метод info, який повертає словник з ключами 'name', 'age' і 'address', та 
значення яких дорівнюють відповідним властивостям екземпляра класу.

Реалізувати для класу Dog атрибут owner, який буде екземпляром класу Owner. Додати до класу Dog метод who_is_owner, 
який повертає результат виклику методу info екземпляра класу Owner, тобто це словник з ключами name, age та address 
власника.
"""


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {"Name": self.name, "Age": self.age, "Address": self.address }


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()


owner = Owner("Sherlock", 24, "London, 221B Baker Street")
dog = Dog("Barbos", 23, "labrador", owner)
print("\n", "*" * 15, " ", "Exercise 7", " ", "*" * 15, "\n")
print(dog.nickname, dog.breed, dog.weight, dog.say())
print(owner.name, owner.age, owner.address)
print(cat.nickname, cat.weight, cat.breed, cat.owner.name, cat.owner.address)
print(dog.who_is_owner())


# Exercise 8
"""
Створіть два класи: CatDog та DogCat. Ці класи повинні наслідуватись від двох класів відразу: Cat та Dog. Після 
успадкування в екземпляра класу CatDog, батьківський метод say повинен повертати "Meow", а у класу DogCat — "Woof". 
Для обох зазначених класів реалізуйте метод info, який повертає рядок у наступному форматі 
f"{self.nickname}-{self.weight}".
"""
print("\n", "*" * 15, " ", "Exercise 8", " ", "*" * 15, "\n")

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"
    def info(self):

        f"{self.nickname}-{self.weight}"


class Dog(Animal):
    def say(self):
        return "Woof"

class CatDog(Cat, Dog):
    def say(self):
        return super().say()
    def info(self):
        return f"{self.nickname}-{self.weight}"

class DogCat(Dog, Cat):
    def say(self):
        return super().say()
    def info(self):
        return f"{self.nickname}-{self.weight}"
