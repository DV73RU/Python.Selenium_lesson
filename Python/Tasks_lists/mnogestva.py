# Словарь (ключ:значение)
famely_3 = {"Папа": "Alex", "Мама": "Olga", "Сын": "Semen", "Доч": "Nasty"}
# print(famely_3["Папа"])


k = famely_3.items()
v = famely_3
name = [k for k in famely_3]
print(f"Список имен {name}")
dolg = [v for v in famely_3]
print(f"Список должностей {dolg}")
# # k = famely_3.items()
# print(name)
# for k, v in famely_3.items():    # "k" - ключ, "v" - значение
#     # print(k)
#     # print(v)
#     # print(f"Должность - {k}, Имя - {v}")

# # Создать списки имён и должностей.
#     name = [k for k in famely_3]
# # # k = famely_3.items()
#     print(name)
