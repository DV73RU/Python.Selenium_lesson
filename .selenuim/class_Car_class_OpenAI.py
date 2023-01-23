""".."""


class Car():

    def __init__(self, model, year, engine_volume, price, mileage, number_of_wheels=4):
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.price = price
        self.mileage = mileage
        self.number_of_wheels = number_of_wheels


car1 = Car('BMW', 2020, 3.0, 55000, 20)


class Truck(Car):
    def __init__(self, model, year, engine_volume, price, mileage):
    
        super().__init__(model, year, engine_volume, price, mileage)
        self.number_of_wheels = 8


truck1 = Truck('MAN', 2020, 5.0, 85000, 10)


def get_information(self):
    return f"model: {self.model}\nyear: {self.year}\nengine_volume: {self.engine_volume}\nprice: {self.price}\nmileage: {self.mileage}\nnumber_of_wheels: {self.number_of_wheels}"
