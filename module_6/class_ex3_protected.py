E
class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active # method is_active is used for reading a protected attribute _is_active

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active


p = Person("Boris", 34, True)
print(p.name, p.age, p.is_active())
print(p.greeting())
print(p.name, p.age, p.is_active())
