class Car():
    def __init__(self, model: str, year: int,wheels: int):
        self.model = model
        self.year = year
        self.wheels = wheels

# A class can have methods, i.e. something it
# can do

    def drive(self) -> None:
        print(f'{self.model} is driving')

    def stop(self) -> None:
        print(f'{self.model} has stopped')


