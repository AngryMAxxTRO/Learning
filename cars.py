import copy
class Car:
    pass

car_1 = Car()
car_1.wheel = 4
car_2 = car_1
car_2.wheel = 3
print(car_1.wheel)

car_3 = copy.copy(car_1)
car_3.wheel = 6
print(car_1.wheel)
