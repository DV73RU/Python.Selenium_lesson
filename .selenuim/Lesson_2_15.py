# lesson_2_14
"""Цикл While."""


# a = 10

# while a > 1:
#     # a = a - 1
#     # b = a
#     # print(a)
#     lists = [a-1 for i in range(a) for y in range(a-1)]
#     print(lists)


tmp = []
for x in range(0, 1):
    for y in range(0, 11):
        tmp.append(x + y)
print(tmp)
