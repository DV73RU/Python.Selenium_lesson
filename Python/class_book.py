"""Классы."""


class Dog():
    """Простая модель собаки."""

    # Метод __init__ с тремя параметрами self, name, age.
    def __init__(self, name, age):
        """Инициализирует атрибуты name, age."""
        self.name = name
        self.age = age

    def sit(self):  # Добавление нового метода sit(сидеть)
        print(f"{self.name} умеет садиться по команде")

    def roll(self):     # Добавление нового метода roll(крутиться)
        print(f"{self.name} умеет крутиться по команде")


my_dog = Dog('Bim', 4)     # Экземпляр конкретной собаки
yor_dog = Dog('Люси', 7)
my_dog.sit()    # Вызов нового метода 
my_dog.roll()
print(my_dog.__dict__)  # Печать всех атрибутов
print(yor_dog.__dict__)
print(f"Имя моей собакти: {my_dog.name}")
print(f"Возраст моей собаки: {my_dog.age}")
my_dog.sit()
print(f"Имя твоей собакти: {yor_dog.name}")
print(f"Возраст твоей собаки: {yor_dog.age}")
