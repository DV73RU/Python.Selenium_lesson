"""Start."""

import hello
import math
import random
from mode import math   #Из папки mode импортируем (пероритетные модули чем стандартные библиотеки)
hello.some()
print(math.pi)  #Печатаем переменную из изпортированного модуля
r = random.randrange(0, 100)
print(r)
user = "User"
print(user + str(random.randrange(0, 100)))
