# lesson_2_14
"""Цикл Генератор списков."""


# a = 10

# while a > 1:
#     # a = a - 1
#     # b = a
#     # print(a)
#     lists = [a-1 for i in range(a) for y in range(a-1)]
#     print(lists)

# [выражение for val in коллекция]

tmp = []
for x in range(0, 1):
    for y in range(0, 11):
        tmp.append(x + y)
print(tmp)

li = [0 for i in range(7)]     # семь раз подставляем "0"
print(li)
li_2 = [i for i in range(10)]
print(li_2)     # "i" принимает значения от 0 до 9 

li_3 = [i**2 for i in range(10)]
print(li_3)     # "i" принимает значения квадрат

li_4 = [i%4 for i in range(1, 15)]
#    остатки делегы на 4   пределы  
print(li_4)

li_5 = [i for i in "Привет"]    # Обходим элемент "Привет" и забераем все его элементы
print(li_5)

li_6 = [i  for i in (-10, 10)]    # Гениреруем список - 10 10
print(li_6)

b = [elem + 1 for elem in li_6]     # герерируеим список прибавля 1 к элементам списка "li_6"
print(b)

li_7 = [i  for i in range(-10, 10)]    # Генерируем список в диаппазоне -10 10
print(li_7)
s = [elem for elem in li_7 if elem%2 == 0]  # Если едементы списка li_7 делятся без остатка на 2(четные) сгенерировать из них новый списолк s
print(s) # Вывод нового списка

v = input().split()
v = [int(i) for i in v]     # Обходим все введенные выражения и преобразуем их в инт значения
print(v)
