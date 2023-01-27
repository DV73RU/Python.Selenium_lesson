"""Импортирование классов."""

from car import Car

my_new_car = Car("Audi", "a4", 2022)
print(my_new_car.get_desprictive_name())

my_new_car.odometr_reading = 13
my_new_car.read_odometr()