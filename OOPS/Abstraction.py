    #abstract = Used to define abstract classes and methods.
        #                   Abstraction is the process of hiding implementation details
        #                   and showing only the essential features.
        #                   Abstract classes CAN'T be instantiated directly.
        #                   Can contain 'abstract' methods (which must be implemented)
        #                   Can contain 'concrete' methods (which are inherited)

from abc import ABC, abstractmethod
import math

#Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def display(self):
        print("This is a shape")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
c = Circle(2)
t = Triangle(3, 4)
r = Rectangle(4, 5)

c.display()
t.display()
r.display()

print(c.area())
print(t.area())
print(r.area())
        

