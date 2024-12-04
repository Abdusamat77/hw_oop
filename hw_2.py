# Базовый класс Vehicle
# class Vehicle:
#     def __init__(self, name, max_speed):
#         self.name = name  # Название транспортного средства
#         self.max_speed = max_speed  # Максимальная скорость

#     def display_info(self):
#         print(f"{self.name} имеет максимальную скорость {self.max_speed} км/ч")


# # Класс-наследник Car (Автомобиль)
# class Car(Vehicle):
#     def display_info(self):
#         print(f"Автомобиль {self.name} может ехать с максимальной скоростью {self.max_speed} км/ч")


# # Класс-наследник Bicycle (Велосипед)
# class Bicycle(Vehicle):
#     def display_info(self):
#         print(f"Велосипед {self.name} может ехать с максимальной скоростью {self.max_speed} км/ч")


# # Создание объектов и вызов методов display_info
# car = Car("Toyota", 180)
# bicycle = Bicycle("Trek", 45)

# car.display_info()  
# bicycle.display_info()  


"ДЗ заданное на уроке"

# Базовые классы

class Animal:
    def __init__(self, name):
        self.name = name  

    def eat(self):
        print(f"{self.name} ест")

    def sleep(self):
        print(f"{self.name} спит")


class Walker:
    def walk(self):
        print(f"{self.name} ходит")


class Swimmer:
    def swim(self):
        print(f"{self.name} плавает")


class Flyer:
    def fly(self):
        print(f"{self.name} летает")



class Penguin(Animal, Walker, Swimmer):
    def __init__(self, name):
        Animal.__init__(self, name) 
        self.name = name  

    def describe(self):
        print(f"{self.name} может ходить и плавать")


class Duck(Animal, Walker, Swimmer, Flyer):
    def __init__(self, name):
        Animal.__init__(self, name)  
        self.name = name  

    def describe(self):
        print(f"{self.name} может ходить, плавать и летать")


class Bat(Animal, Flyer):
    def __init__(self, name):
        Animal.__init__(self, name) 
        self.name = name  

    def describe(self):
        print(f"{self.name} может летать")



penguin = Penguin("Пингвин")
duck = Duck("Утка")
bat = Bat("Летучая мышь")

penguin.describe() 
# penguin.walk()  
# penguin.swim()  
# penguin.eat()  
# penguin.sleep() 

duck.describe()  
# duck.walk()
# duck.swim() 
# duck.fly()
# duck.eat()  
# duck.sleep() 

bat.describe()  
# bat.fly()
# bat.eat() 
# bat.sleep() 
