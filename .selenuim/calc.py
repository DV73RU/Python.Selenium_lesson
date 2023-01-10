"""Калькулятор"""


# from termcolor import colored, cprint

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print("Какие действия с числами выполнить? ")
inn = input(
    "Нажмите: '/' - деление, '*' - умножение, '+' - сложение, '-' - вычитание, 'x' - выход :")
if inn == str('/'):
    try:
        result = int(a / b)
    except ZeroDivisionError:
        result = 0
    print("\033[4m\033[37m\033[41m{}\033[0m".format("На ноль делить нельзя"))
else:
    print(f"Результат деления: {a} на {b} равен: {result}")
