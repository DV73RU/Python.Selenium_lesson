# lesson_2_14
"""Цикл for."""
"""Выводим имена из списка в кторых 4 символа"""
students = ["Alex", "Ivan", "Nasty", "Olga", "Semen", "Igor", "Svetlan"]

for f in students:
    if len(f) == 4:     # Найти имена в списке с 4 буквами
        print(f + " - в имени 4 буквы")    # Вывести имена с 4 буквами


students = ["Alex", "Ivan", "Nasty", "Olga", "Semen", "Igor", "Svetlanа"]
s = len(students)
for f in students:
    s == 4   # Количество знаков в элементе
    students.remove(f)     # Найти имена в списке с 4 буквами
    print(f, students)


# Подчитать количество знаков в каждом элементе и вывести

students = ["Alex", "Ivan", "Nasty", "Olga", "Semen", "Igor", "Svetlanа"]
for i in range(len(students)):
    
    print(i, students[i])
    print("--------------------")


students = ["Alex", "Ivan", "Nasty", "Olga", "Semen", "Igor", "Svetlanа"]
print(f"Количество имен в списке - {len(students)}")    # Количество элементов в списке

for i in students:
    s = len(i)
    # print(f'{i} = {len(i)}')
    print(f'{i} = {s}') # Выводим количество знаков в каждом элементе списка



