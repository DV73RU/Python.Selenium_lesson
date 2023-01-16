"""Классы."""


class Car():
    """Класс автомобиль."""

    # Метод __init__ с четырмя параметрами first_name, last_name....
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описание автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 100

    # Добавление нового метода discribe_restarant.
    def get_desprictive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def update_odometr(self, miliage):
        """Устанавливает значение одометра."""
        if miliage >= self.odometr:
            self.odometr = miliage
        else:
            print("Попытка усменьшить одометр")

    def increated_odometr(self, miliage):
        """Увеличивает значение одометра с заданным припращением."""
        self.odometr += miliage

    def read_odometr(self):
        """Выводит значение одометра."""
        print(f"У автомобиля пробег стостовляет: {self.odometr} мили")


my_new_car = Car('audi', 'a4', 2019)
my_esed
print(my_new_car.get_desprictive_name())
# my_new_car.odometr = 2000
my_new_car.update_odometr(101)
my_new_car.read_odometr()

