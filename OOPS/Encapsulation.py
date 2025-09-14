class Car:
    def __init__(self,make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    #getters
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year
    
    #setters
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

car = Car("Chevrolet", "Camaro", 2021)
print(car.get_make())
print(car.get_model())
print(car.get_year())
car.set_year(2022)
print(car.get_year())