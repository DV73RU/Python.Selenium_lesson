"""Классы."""


class Car():
    """Класс пользователь."""

    # Метод __init__ с четырмя параметрами first_name, last_name....
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описание автомобиля."""
        self.make = make
        self.model = model
        self.year = year

    def ger_desprictive_name(self):  # Добавление нового метода discribe_restarant.
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.make} {self.model} {self.year}"

