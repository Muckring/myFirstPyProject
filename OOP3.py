from animals import *

def main() -> None:

    dog = Dog("Rex")
    cat = Cat("Tim")
    rabbit = Rabbit("Roger")

    animals: list[Animal] = [dog, cat, rabbit]

    for animal in animals:
        animal.eat()
        animal.sleep()
        animal.shit()
        print("******************")

if __name__ == '__main__':
    main()
