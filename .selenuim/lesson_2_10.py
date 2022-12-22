# lesson_2_10
"""Область видимости переменных."""


var_1 = 10  # Глобальная переменная
var_2 = 20  # Глобальная переменная


def sum(var_1, var_2):
    """sum."""
    var_1 = 30  # Локальная переменная
    var_2 = 40  # Локальная переменная
    result = var_1 + var_2
    return result


print(var_1, var_2)
p = sum(var_1, var_2)

print(p)
