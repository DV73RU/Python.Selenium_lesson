# lesson_2_18
"""2.18 Работа со словарями и множествами"""

# Список
famely_1 = ["Alex", "Ivan", "Nasty", "Olga", "Semen", "Igor", "Alex"]
print(famely_1)

# Множества
famely_2 = {"Alex", "Ivan", "Nasty", "Olga", "Semen", "Igor", "Alex"} 
print(famely_2)


# Словарь (ключ:значение)
famely_3 = {"Папа": "Alex", "Мама": "Olga", "Сын": "Semen", "Доч": "Nasty"}
# print(famely_3["Папа"])
for k, v in famely_3.items():    # "k" - ключ, "v" - значение
    # print(k)
    # print(v)
    print(f"Должность - {k}, Имя - {v}")

# Создать списки имён и должностей.
