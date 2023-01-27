# lesson_2_13_задачи
"""Задача (списки)."""

frends = ["Алексей", "Антон", "Юра", "Саша", "Данила"]
print(frends[0])
print(frends[1])
print(frends[2])
print(frends[3])
print(frends[4])

print(len(frends))  # Считаем количество элементов в списке

frends.append("Саша")    # Добавляем новой элемент списка (.apped)
frends.append("Анатолий")
print(len(frends))
print(len(frends))   # Считаем новое количество элементов в списке
sum = f"Всего друзей - {len(frends)}."  # Функция присваивает количество элементов
print(sum)  # Выводим количество элементов


message = f"Имя крайнего друга - {frends[-1]}"

print(message)  # Выводим текст и последний в списке элемента

element = len(frends)   # Присваиваем перменой значение количества элементов в списке
if element > 5:
    print("Увас больше 5 друзей")
else:
    print("У Вас мало друзей")

message = f"Имя первого друга - {frends[0]}"
print(message)
