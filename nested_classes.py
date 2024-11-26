# This file contains info about nested classes in Python

class Car:

    class Engine:
        
        def __init__(self, horsepower):
            self.horsepower = horsepower

        def display_details(self):
            return f"{self.horsepower} hp"

    class Wheel:
        
        def __init__(self, size):
            self.size = size

    def __init__(self, make, model, year):
        
        self.make = make
        self.model = model
        self.year = year
        self.engines = []
        self.wheels = []

    def __str__(self):
        return f'Make: {self.make} Model: {self.model} Year: {self.year}'

    def add_engine(self, horsepower):
        new_engine = self.Engine(horsepower)
        self.engines.append(new_engine)

    def display_engine(self):
        return [engine.display_details() for engine in self.engines]

car = Car("Lada", "Kalina", 2021)

car.add_engine(500)
for engine in car.display_engine():
    print(engine)

