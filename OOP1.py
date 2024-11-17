class Car():
    def __init__(self, model: str, year: int,wheels: int):
        self.model = model
        self.year = year
        self.wheels = wheels

car1 = Car("Honda", 1998, 4)
print(car1.model)
print(car1.year)
print(car1.wheels)
