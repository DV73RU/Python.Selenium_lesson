# lesson_2_14
"""Цикл While."""


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

li_4 = [i**2 for i in range(10)]
print(li_5)     # "i" принимает значения квадрат