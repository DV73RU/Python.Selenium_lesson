# lesson_2_10
"""Область видимости переменных."""


var_1 = 100  # Глобальная переменная
var_2 = 20  # Глобальная переменная?


def sum():
    """sum."""
    # var_1 = 30  # Локальная переменная
    # var_2 = 40  # Локальная переменная
    result = var_1 + var_2
    print(result)


def sub():
    """sum."""
    # var_1 = 100  # Локальная переменная
    # var_2 = 40  # Локальная переменная
    result = var_1 - var_2
    print(result)


sum()   # Вызываем функцию сложения def sum
sub()   # Вызываем функцию сложения def sum


# print(var_1, var_2)
# p = sum(var_1, var_2)
# p1 = sub(var_1, var_2)

# print(p)
# print(p1)