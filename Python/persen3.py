"""Ццвета и диаметры кружков
"""


class Point:
    color = 'red'
    circus = 2


print(f'Параметры (атрибуты) Point: {Point.color} и {Point.circus}')     # Выводим атрибуты класс Point
# a = Point()
# b = Point()
# print(a)
# print(b)

in_a = int(input("ведити новый параметр circus:  "))
in_b = str(input("ведити новый параметр color:  "))

Point.circus = in_a
Point.color = in_b
print(f'Новые параметры (атрибуты) Point: {Point.color} и {Point.circus}')

print(Point.__dict__)   # Все обьекты класса 
