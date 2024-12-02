

class Person:

    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age
    
    @property

    def get_name(self):
        return self._name

    @property

    def get_age(self):
        return self._age

    
    

    
