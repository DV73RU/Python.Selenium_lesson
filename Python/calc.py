"""Калькулятор"""

# Запилить выбор действия через списки
# from termcolor import colored, cprint
# ValueError

try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
except ValueError:
    print("Это не число!")
else:
    print("Какие действия с числами выполнить? ")
    inn = input("Нажмите:\n'/' - деление,\n'*' - умножение,\n'+' - сложение,\n'-' - вычитание,\n'x' - выход\n")
    if inn == str('/'):
        try:
            result = int(a / b)
        except ZeroDivisionError:
            result = 0
            print("\033[4m\033[37m\033[41m{}\033[0m".format("На ноль делить нельзя"))
        else:
            print(f"Результат деления: {a} на {b} равен: {result}")
    elif inn == str('*'):
        result = int(a * b)
        print(f"Результат умножение: {a} на {b} равен: {result}")
    elif inn == str('+'):
        result = int(a * b)
        print(f"Результат сложения: {a} и {b} равен: {result}")
    elif inn == str('-'):
        result = int(a - b)
        print(f"Результат вычитания: {b} из {a} равен: {result}")
    elif inn == str('x'):
        quit()
