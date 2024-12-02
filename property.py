import time

class Person:

    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age
    
    @property

    def person_name(self):
        return self._name

    @property

    def person_age(self):
        return self._age

    @person_name.setter

    def person_name(self, new_name: str) -> str | None:
        print(f'Changing name to {new_name}')
        time.sleep(4)
        self._name = new_name

    @person_age.setter

    def person_age(self, new_age: int) -> int | None:
        print(f'Changing age to {new_age}')
        time.sleep(4)
        self._age = new_age

    @person_name.deleter

    def person_name(self):
        print(f'Deleting {self._name}')
        del self._name
        time.sleep(4)
        print('Name has been successfully deleted')

person1 = Person("Kostya", 41)
person1.person_name = "Konstantin"
print(person1.person_name)

del person1.person_name



    
    

    
