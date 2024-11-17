from OOP1 import Car

car1 = Car("Volvo", 1999, 4)
car2 = Car("Porsche", 1973, 4)
car3 = Car("BMW", 1984, 4)

cars: list[Car] = [car1, car2, car3]

for car in cars:
    print()
    print(f'{car.model}')
    print(f'{car.year}')
    print(f'{car.wheels}')
    car.drive()
    car.stop()
    print()