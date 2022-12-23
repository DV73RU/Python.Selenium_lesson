# lesson_2_12_operator
"""Условные операторы: if, else, elif."""


age = 26
name = "Ale"
if age == 25 and name == "Alex":
    print("Вам 25 лет и зовут Alex")
elif age > 25 and name != "Alex":
    print("Вам больше 25 лет и вы не Alex")

else:
    print("Мне меньше 25 лет")
