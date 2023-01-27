# lesson_2_13_списки
"""Списки."""


personal = ["Alex", "Ivan", "Nasty", "Olga"]     # Список.
#              0      1        2        3
result = personal[0] + " + " + personal[2]    # Взять первый элемент списка и сложить со вторым элементом скипска.
print(result + " - Лучшая пара")  # Вызываем из списка результат сложения и фраза (константинация).
number = [1, 15, 23, 4]     # Список из цифр.
#         0   1   2   3
print(number[2])    # Выводим из списка второй элемент.
result_num = number[0] + number[2]  # Складывавем элементы из списка 0 и 2.
print(result_num)    # Выводим результат сложения.

num_1 = number[0]   # Переменная хранит значениея из списков
num_2 = number[2]    # Переменная хранит значениея из списков
rez = num_1 + num_2    # Складываем переменные
print(rez)  # Выводим результат сложения

print(len(personal))    # Считаем количиство елементов в списке
print(personal[-1])     # Обратиться к послендниму элемнту списка
personal.append("Fedor")
print(personal)

pn = []
pn.append(personal)
pn.append(number)
print(pn)


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(number)   # выводми список
print(number[:5])   # C 0 по 4
print(number[5:])   # C 5 до конца
print(number[5:10])     # C 5 до 9
print(number[::5])      # Шаг 5
print(number[1::3])     # C начиная с 1 и шагом 3
print(number[:-4])      # Все кроме 4 последних
print(number[1:-1])     # Без первого и последнего
print(number[::-1])     # Реверс списка
print(number[::-2])     # Реверс с шагом 2
print(number[-2::-2])   # Реверс с 2 с конца и щагом 2
print(number[10::-15])
