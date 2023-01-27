"""Классы."""


class Car():
    """Класс автомобиль."""

    # Метод __init__ с четырмя параметрами first_name, last_name....
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описание автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0

    # Добавление нового метода discribe_restarant.
    def get_desprictive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometr(self):
        """Выводит значение одометра."""
        print(f"У автомобиля пробег стостовляет: {self.odometr_reading} мили")

    def update_odometr(self, miliage):
        """Устанавливает значение одометра."""
        if miliage >= self.odometr_reading:
            self.odometr_reading = miliage
        else:
            print("Попытка усменьшить одометр")


class ElectricCar(Car):
    """Представляет аспекты машины, спецефические для электромобиля."""

    def __init__(self, make, model, year):
        """инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)
        self.batt_suse = 2000

    def describe_batt(self):
        print(f"Ескость акумулятора: {self.batt_suse} mAch")


my_tesla = ElectricCar('tesla', 'model S', 2020)
print(my_tesla.get_desprictive_name())
my_tesla.describe_batt()
