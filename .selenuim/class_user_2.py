"""Классы."""
# Ппоробовать через списки Имен фамилий изерей.


class User():
    """Класс пользователь."""

    # Метод __init__ с четырмя параметрами first_name, last_name....
    def __init__(self, first_name, last_name, age, gender):
        """Инициализирует атрибуты first_name, last_name, age, gender."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        
    def discribe_user(self):  # Добавление нового метода discribe_restarant.
        """Метод выводит информацию о пользоваетеле."""
        print(f"{self.first_name} {self.last_name} {self.age} {self.gender}")

    def gret_user(self): 
        """Метод выводит приветствие пользователя."""
        print("Добро пожаловать")


user = User("Анатолий", "Иванов", 45, "Мужчина")
user_1 = User("Сергей", "Петров", 23, "Мужчина")
user_2 = User("Марина", "Павлова", 43, "Женщина")
user.gret_user()
user.discribe_user()

user_1.gret_user()
user_1.discribe_user()
user_2.gret_user()
user_2.discribe_user()
