# lesson_2_6_2_str
"""Строчные типы данных."""

# str_1 = "hello"
# str_2 = "WORLD"
# print(str_1)
# print(dir(str_1))   # Выводим список всех функций которые можно применить к данной функции
# print(str_1.upper())    # Выводим переменну с переводом в верхний регистр
# print(str_1.title())    # Выводим значение переенной первая буква с верхнего регистра
# print(str_2.lower())    # Выводим значение переменной всё в нижнем регистре

# name = input(str)   # Присваиваем перемменой значение.
# s = "Hello {}"  # Присваиваем переменной значение с возможностью вставки в значение
# result = s.format(name)  # Переменная принимаени згачение переменной "a" и вставка значение переменной "name"
# print(result)   # Выводим на печать значение переменной


first_name = str(input("Введите имя :"))
last_name = str(input("Введите фамилию :"))
a = '{} {}'     # 1
result_2 = a.format(first_name, last_name)  # 2
print("Привет :" + result_2.title)    # Константинация

result_3 = f'{first_name} {last_name}'   # Аналогичнго как 1 и 2
print("Прив :" + result_3.title())  # Выводит результат первая буква в верхнем регистре + константинаци
