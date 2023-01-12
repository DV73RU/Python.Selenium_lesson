class Person():
    """Создаём человека"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.wight = 50

    def description_person(self):
        """Получение описание человека"""

        description = self.name + " ему " + \
            str(self.age) + " лет " + str(self.height) + " <- его рост, " + str(self.wight) + " < - его вес"
           
        print(description)
    
    def get_wieght(self):
        """Получение веса человека"""
        print("Вес нашего человека : " + str(self.wight))
        
    def update_wieght(self, kg):
        """Изменение веса человека"""
        self.wight = kg



man = Person("Alex", 20, 180)
# man.wight = 11
# man.description_person()

man.update_wieght(123)
man.get_wieght()