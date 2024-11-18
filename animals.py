

class Animal:
    def __init__(self, name: str):
        self.name = name
    def eat(self) -> None:
        print(f'{self.name} is eating')
    def sleep(self) -> None:
        print(f'{self.name} is asleep')
    def shit(self) -> None:
        print(f'{self.name} is taking a shit')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Rabbit(Animal):
    pass