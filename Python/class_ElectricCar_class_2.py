"""Классы."""


class Car():
    """Класс автомобиль."""

    # Метод __init__ с четырмя параметрами first_name, last_name....
    def __init__(self, make, model, year, ):
        """Инициализирует атрибуты описание автомобиля: модель, год выпуска, объем двигателя, цена, пробег, количество колес = 4."""
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


class Battery():
    """Модель аккумулятора"""

    def __init__(self, battary_size=100):
        self.battary_size = battary_size
        """Инициализирует размер батарееи."""
    
    def discrabe_battary(self):
        """Выводит информацию о ескости батареи."""
        print(f'Ёмкость батарее равно: {self.battary_size} mAch')
    
    def get_range(self):
        if self.battary_size == 75:
            range = 260
        elif self.battary_size == 100:
            range = 316
        print(f'Эта машина проедет {range} км. на полной зарядки.')
    
    def update_range(self):

class ElectricCar(Car):
    """Представляет аспекты машины, спецефические для электромобиля."""

    def __init__(self, make, model, year):
        """инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специальные для электромобиля
        """
        super().__init__(make, model, year, get_batte)
        self.get_batta = 1200

    # def describe_batt(self):
    #      print(f"Ескость акумулятора: {self.battary_size} mAch")


my_tesla = ElectricCar('tesla', 'model S', 2020)
print(my_tesla.get_desprictive_name())
my_tesla.describe.discrabe_battary()
my_tesla.describe.get_range()

