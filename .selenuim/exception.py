"""Исключения"""

a = int(input("Введите первое знаечение: "))
b = int(input("Введите второе значение: "))


try:
    result = int(a / b)
except ZeroDivisionError:
    result = 0
    print("На ноль делить нельзя")
print(f"Результат : {result}")
print("Результат : " + str(result))
result_2 = a + b
print(result_2)
# print(type(result))

# ZeroDivisionError