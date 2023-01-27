
class Person():
    """Человек"""

    def __init__(self, name, age):
        self.name = name    # имя человека
        self.age = 0      # возраст человека

    def display_info(self):
        print(f"Имя: {self.name}  Возраст: {self.age}")


tom = Person("Tom", 0)
tom.age = 37
tom.display_info()      # Name: Tom  Age: 37

bob = Person("Bob", 0)
bob.age = 41
bob.display_info()      # Name: Bob  Age: 41
