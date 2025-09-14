class Car:
    def go(self):
        print("You drive the car")

class Bike:
    def go(self):
        print("You ride the bike")

class Boat:
    def go(self):
        print("You sail the boat")

car = Car()
bike = Bike()
boat = Boat()
vehicles = [car, bike, boat] 

for vehicle in vehicles:
    vehicle.go() #run-time


#compile-time polymorphism
class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

#Create object
calc = Calculator()

#Using default arguments
print(calc.multiply())            
print(calc.multiply(4))           

#Using multiple arguments
print(calc.multiply(2, 3))       
print(calc.multiply(2, 3, 4))

#Runtime polymorphism
class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())