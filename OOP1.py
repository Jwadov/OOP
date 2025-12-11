# Abstraction & Encapsulation
class Animal:
    def __init__(self, name, sound):
        self.__name = name
        self.__sound = sound

    def make_sound(self):
        print(f"{self.__name} says {self.__sound}")

# Inheritance
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

# Polymorphism
animals = [Dog("Rex"), Cat("Luna")]

for animal in animals:
    animal.make_sound()