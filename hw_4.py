
class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name  # Название транспортного средства
        self.max_speed = max_speed  # Максимальная скорость

    def calculate_travel_time(self, distance):
        return 0

    def display_info(self):
        print(f"Тип транспорта: {self.__class__.__name__}, Название: {self.name}, Максимальная скорость: {self.max_speed} км/ч")

class Car(Vehicle):
    def calculate_travel_time(self, distance):
        """ Метод для расчета времени путешествия на автомобиле """
        return distance / self.max_speed

class Bicycle(Vehicle):
    def calculate_travel_time(self, distance):
        """ Метод для расчета времени путешествия на велосипеде (с дополнительными остановками) """
        base_time = distance / self.max_speed
        return base_time * 1.2  # увеличиваем время на 20%

class Plane(Vehicle):
    def calculate_travel_time(self, distance):
        """ Метод для расчета времени путешествия на самолете с учетом взлета и посадки """
        base_time = distance / self.max_speed
        takeoff_landing_time = 1 
        return base_time + takeoff_landing_time

def calculate_and_display_travel(vehicle, distance):
    vehicle.display_info()  # Вывод информации о транспорте
    travel_time = vehicle.calculate_travel_time(distance)  # Расчет времени
    print(f"Время в пути для {vehicle.name} на расстояние {distance} км: {travel_time:.2f} часов\n")


car = Car("Toyota", 120)
bicycle = Bicycle("Giant", 25)
plane = Plane("Boeing 737", 800)

distance = 500
calculate_and_display_travel(car, distance)
calculate_and_display_travel(bicycle, distance)
calculate_and_display_travel(plane, distance)
