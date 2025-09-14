#Base class
class Organism:
    def __init__(self):
        self.is_alive = True

#Subclass of Organism
class Plant(Organism):
    def photosynthesize(self):
        print("The plant absorbs sunlight")

#Subclass of Organism
class Animal(Organism):
    def eat(self):
        print("This animal is eating")

#Subclass of Animal
class Dog(Animal):
    def __init__(self):
        super().__init__() #calls parent constructor
        self.lives = 1

    def speak(self):
        print("The dog goes *woof*")

#Subclass of Animal
class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.lives = 9

    def speak(self):
        print("The cat goes *meow*")

dog = Dog()
cat = Cat()
plant = Plant()

print(dog.is_alive) #inherited from Organism
dog.eat()           #inherited from Animal
dog.speak()

print(cat.is_alive)
cat.eat()
cat.speak()

print(plant.is_alive)
plant.photosynthesize()
