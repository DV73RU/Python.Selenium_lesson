class Person():
    """Модель человека"""

    def __init__(self, name, age):
        """Инициализация адрибутов человека - имя, возраст"""
        self.name = name
        self.age = 1
        print("Человек создан")

    def sing(self):
        """Просим человека спеть"""
        print(self.name + " Поёт")

    def dens(self):
        """Просим человека с танцевать"""ы
        print(self.name + " Танцует")

    def _info(self):
        print(f"Имя: {self.name} Возраст {self.age}")


man = Person("Алекс")
man.age = 37
man_2 = Person("Толя")
man_2.age = 40
man._info()
man_2._info()
# print(man.name)
man.dens()
man_2.sing()
