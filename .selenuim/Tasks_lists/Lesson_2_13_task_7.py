# lesson_2_13_задачи
"""Задача (Удаление в списке элемента 'remov')."""
"""Удаление элемента по значению."""

# frends = ["Алексей", "Антон", "Юра", "Саша", "Данила"]  # Списорк друзей
# print(frends)   # Вывод списка друзей
# frends[0] = "Семён"     # Измение в список первым лементом
# print(frends)   # Вывод нового списка

moto = ["honda", "yamaha", "suzuki"]
print(moto)
tool_moto = "honda"
moto.remove(tool_moto)    # Удаление элемента со хначением "honda"
print(moto)
print(f"\nМотоцикл {tool_moto.title()} сломался")
