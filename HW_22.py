class Vehicle:
    def __init__(self,name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display_info(self):
        print(f"{self.name} имеет максималбную скорость {self.max_speed} км/ч")

class Car(Vehicle):
    def display_info(self):
        print(f"Автомобиль {self.name} может ехать с максимальной скоростью {self.max_speed} км/ч")

class Bicycle(Vehicle):
    def display_info(self):
        print(f"Велосипед {self.name} может ехать с максимальной скоростью {self.max_speed} км/ч")

car = Car('Bmw', 260)
bicycle = Bicycle("bmx", 45)

car.display_info()
bicycle.display_info()