# lesson_2_9_2
"""Что такое функции и работа с ними."""

name = str(input("Введити ваше имя :"))
age = int(input("Суколько вам лет? :"))
man = age * 12


def his(name, man):     # Обявление функции включает агрумент name age
    """dd."""
    result = "Привет " + name + " тебе " + str(man) + " месяца "   # Печать результата
    return result


h = his(name, man)
print(h)
