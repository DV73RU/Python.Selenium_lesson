# lesson_2_5
"""Числовые типы данных."""


num_1 = 5   # num_1 - не равно 5 а переменной присвоено значение "5"
num_1 = 10  # перезаписываем значение переменой num_1 c "5" на "10"
print(type(num_1))  # выводим тип переменной
print(num_1)  # выводим значение переменной

num_1 = 7   # num_1 - не равно 5 а переменной присвоено значение "5"
num_2 = 5  # num_2 - не равно 10 а переменной присвоено значение "10"
result = num_1 + num_2  # Переменная принимает значение суммы двух переменных
result_1 = num_1 - num_2    # Вычитание
result_2 = num_1 * num_2    # Умножение
result_3 = num_1 ** 2   # Возведение в степень 2
result_4 = num_1/num_2  # Деление
result_5 = num_1 // num_2   # Деление без остатка
result_6 = num_1 % num_2    # Остаток от деления

print(result)   # Выводим результат сложения
print(result_1)
print(result_2)
print(result_3)
print(result_4)    # Выводим результат деления
print(int(result_4))    # Выыодит целое значение результата деления
print(result_5)   # Выводит результат деление без остатка
print(result_6)  # Выводит остаток от деления
print(num_1 == num_2)   # Выводим проверку равенста значение переменных
print(num_1 < num_2)   # Выводим проверку не равенста значение переменных
print(num_1 > num_2)   # Выводим проверку не равенста значение переменных
print(num_1 >= num_2)   # Выводим проверку больше или равно значение переменных
print(num_1 <= num_2)   # Выводим проверку меньше или равно значение переменных
print(round(10/3))  # Округление
print(round(10/3, 4))  # Округление до 4 знака.