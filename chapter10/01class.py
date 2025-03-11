#basics of class and object
# problem create a car class with attributes like brand and model then create the instance of this class

class Car:
    def __init__(self,brand ,model):
        self.brand=brand
        self.model=model


my_car=Car("Toyota","corolla")    
print(my_car.brand)
print(my_car.model)

my_new_car=Car("mahendra","safari")
print(my_new_car.brand)
print(my_new_car.model)
