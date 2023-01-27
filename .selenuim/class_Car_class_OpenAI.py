"""Наследование калссов."""


class Car():
    """Экземпляр класса автомобиль."""
    def __init__(self, model, year, engine_volume, price, mileage, number_of_wheels=4):
        self.model = model  # Марка
        self.year = year    # Год выпуска
        self.engine_volume = engine_volume  # Обьём двигателя
        self.price = price  # Цена
        self.mileage = mileage  # Пробег
        self.number_of_wheels = number_of_wheels    # Количество колёс

    def get_information(self):
        """"Метод возвращает информацию характеристик автомобиля."""
        return f"model: {self.model}\nyear: {self.year}\nengine_volume: {self.engine_volume}\nprice: {self.price}\nmileage: {self.mileage}\nnumber_of_wheels: {self.number_of_wheels}\n"


car1 = Car('BMW', 2020, 3.0, 55000, 20)


class Truck(Car):
    """Создаём класс грузовик с наследованием от класса автомобиль."""

    def __init__(self, model, year, engine_volume, price, mileage):
        super().__init__(model, year, engine_volume, price, mileage)
        self.number_of_wheels = 8   # Котличестов колёс.


truck1 = Truck('MAN', 2020, 5.0, 85000, 10)


print(car1.get_information())   # Выводим  информацию о машине
print(truck1.get_information())     # Выводим информацию о грузовике
