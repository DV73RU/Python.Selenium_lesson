"""Классы."""


class Restaurant():
    """Ресторан."""

    # Метод __init__ с тремя параметрами self, name, age.
    def __init__(self, resrorant_name, cuisine_type):
        """Инициализирует атрибуты resrorant_name, cuisine_type."""
        self.resrorant_name = resrorant_name
        self.cuisine_type = cuisine_type
        
    def discribe_restarant(self):  # Добавление нового метода discribe_restarant.
        print(f"{self.resrorant_name} {self.cuisine_type}")

    def discribe_restarant_1(self):  # Добавление нового метода discribe_restarant.
        print(f"{self.resrorant_name} {self.cuisine_type}")
    
    def discribe_restarant_2(self):  # Добавление нового метода discribe_restarant.
        print(f"{self.resrorant_name} {self.cuisine_type}")

    def open_rastaran(self):    # Новый метод Открытие или Закрыт ресторан
        print(f"{self.cuisine_type}")
    

restarant = Restaurant("Голубая устрица", "Открыт")
restarant_1 = Restaurant("У Палыча", "Закрыт")
restarant_2 = Restaurant("Метелица", "Открыт")
restarant.discribe_restarant()
restarant_1.discribe_restarant()
restarant_2.discribe_restarant()
restarant.open_rastaran()
restarant_1.open_rastaran()
restarant_2.open_rastaran()






# my_dog = Dog('Bim', 4)     # Экземпляр конкретной собаки
# yor_dog = Dog('Люси', 7)
# my_dog.sit()    # Вызов нового метода 
# my_dog.roll()
# print(my_dog.__dict__)  # Печать всех атрибутов
# print(yor_dog.__dict__)
# print(f"Имя моей собакти: {my_dog.name}")
# print(f"Возраст моей собаки: {my_dog.age}")
# my_dog.sit()
# print(f"Имя твоей собакти: {yor_dog.name}")
# print(f"Возраст твоей собаки: {yor_dog.age}")
