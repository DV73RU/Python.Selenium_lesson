# lesson_2_13_задачи
"""Задача (Удаление в списке элемента 'pop')."""
"""Удаление элемента с возможностью с ней рпботать."""

# frends = ["Алексей", "Антон", "Юра", "Саша", "Данила"]  # Списорк друзей
# print(frends)   # Вывод списка друзей
# frends[0] = "Семён"     # Измение в список первым лементом
# print(frends)   # Вывод нового списка

frends = []   # Создаём новый список
spisok = (len(frends))     # Переменная принимает значения корличества элементов в списке
print(f"У вас {spisok} друзей")     # Выводим количество элементов + Фраза
new_frend = input("Введите имя друга : ")
frends.append(new_frend)  # Переменная принимает вводимое значение
new_frend = input("Введите имя друга : ")
frends.append(new_frend)
new_frend = input("Введите имя друга : ")
frends.append(new_frend)    # Добавляем в список новый элемент введённый с клавиатуры
spisok = (len(frends))  # Перееменная принимает  новое количество элементо списка
print(f"У вас {spisok} друг: ")    # Выводим фрузу с вставкой количества элементов с новым
print(frends)

del frends[1]   # Удаляем второй элемент
print(frends)   # Выводим новый список
