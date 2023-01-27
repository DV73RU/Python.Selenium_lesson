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

    def increated_odometr(self, milis):
        """Увеличивает значение одометра с заданным припращением."""
        self.odometr += milis

    def read_odometr(self):
        """Выводит значение одометра."""
        print(f"У автомобиля пробег стостовляет: {self.odometr} мили")


my_new_car = Car('audi', 'a4', 2023)
print(my_new_car.get_desprictive_name())
my_new_car.update_odometr(101)
my_new_car.read_odometr()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_desprictive_name())
my_used_car.update_odometr(23_500)
my_used_car.read_odometr()

my_used_car.increated_odometr(100)
my_used_car.read_odometr()


