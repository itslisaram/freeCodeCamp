# Classes

class Animal:
    def walk(self):
        print("Walking...")

class Dog(Animal): # Dog class inherits from Animal class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('woof!')

roger = Dog('Roger', 8)

print(roger.name)
print(roger.age)

roger.bark() # No need for a print -> bark() already has a print
roger.walk()