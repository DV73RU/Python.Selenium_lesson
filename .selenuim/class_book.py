"""Классы."""


class Dog:
    """Простая модель собаки."""

    # Метод __init__ с тремя параметрами self, name, age.
    def __init__(self, name, age):
        """Инициализирует атрибуты name, age."""
        self.name = name
        self.name = age
  
my_dog = Dog ('Bim', 4)     # Экземпляр конкретно собаки
print(f"Имя сойё собакти: {my_dog.name}")

