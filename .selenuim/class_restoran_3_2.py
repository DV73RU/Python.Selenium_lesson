"""Классы."""


class Restaurant():
    """Ресторан."""

    # Метод __init__ с тремя параметрами self, name, age.
    def __init__(self, resrorant_name, cuisine_type):
        """Инициализирует атрибуты resrorant_name, cuisine_type."""
        self.resrorant_name = resrorant_name
        self.cuisine_type = cuisine_type
        self.number_served = 10  # Количкство обслуженных клментов.

    # Добавление нового метода discribe_restarant.
    def discribe_restarant(self):
        print(f"{self.resrorant_name} {self.cuisine_type}")

    # Добавление нового метода discribe_restarant.
    def discribe_restarant_1(self):
        print(f"{self.resrorant_name} {self.cuisine_type}")

    # Добавление нового метода discribe_restarant.
    def discribe_restarant_2(self):
        print(f"{self.resrorant_name} {self.cuisine_type}")

    def open_rastaran(self):    # Новый метод Открытие или Закрыт ресторан
        print(f"{self.cuisine_type}")

    def set_number_served(self):  # Новый метод
        """Выводит корличестов обсдуженных клиентов ресторана."""
        print(f"Количество обслуженных клиентов: {self.number_served}")


class IceCreamStand(Restaurant):
    """Киоск с мороженым."""

    def __init__(self, resrorant_name, cuisine_type): # Инициализимруем атрибуты класса родителя
        super().__init__(resrorant_name, cuisine_type)
        self.flavors = 100
       
    def get_flavors(self):
        """Выводим информацию о количтве чортов морорженого."""
        print(f'Количество сортов мороженого в ресторане : {self.flavors} видов.')


restarant = Restaurant("Голубая устрица", "Открыт")
restarant.set_number_served()
restarant_1 = Restaurant("У Палыча", "Закрыт")
restarant_2 = Restaurant("Метелица", "Открыт")
restarant = IceCreamStand("Мороженое и напитки", "Открыт")
restarant.get_flavors()
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
