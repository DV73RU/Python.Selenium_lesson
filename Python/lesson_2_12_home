# lesson_2_12_home
"""Банкомат. Проверяем валидность PIN кода."""
# //TODO Дописать
print("Введите PIN код : ")
pin_bamk = 9876
ostatok_ob = 24890

valids = "Y"
invalid = "N"


def valid():
    user_pin = int(input())
    if user_pin == pin_bamk:
        print("Проверить баланс карты: Y/N")
        print("Какую сумму хоти снять?: ")
        valids = str(input())
        if valids == "Y":
            print("Баланс на карте :", ostatok_ob)
            print("Какую сумму хоти снять?: ")
            sn = int(input())
            ostatok = ostatok_ob - sn
            print("Вы сняли: ", sn)
            print("На карте отстаток: ", ostatok)
            return ostatok_ob
        else:
            valids != "Y"
            print("Выход")
    else:
        print("Ошибка, ввведите корректный PIN код, у вас осталось 3 попытки")
        user_pin = int(input())


valid()



        
        # else:
        #     print("Ошибка, ввведите короектный PIN код, у вас осталось 1 попытка")
        #     user_pin = int(input())
        #     if pin_bamk == user_pin:
        #         print("Проверить баланс карты: Y/N")
        #         print("Какую сумму хоти снять?: ")
        #     else:
        #         print("Ошибка, Ваша карта заблокирована обратитесь в банк")
