class Mammal:
    def __init__(self, species):
        self.animal = species

    def walk(self):
        print(f"{self.animal} is walking")


class Dog(Mammal):
    def bark(self):
        print(self.animal, " is barking")


class Cat(Mammal):
    pass


dog1 = Dog("Dog")
dog1.bark()
cat1 = Cat("Meaow")
cat1.walk()