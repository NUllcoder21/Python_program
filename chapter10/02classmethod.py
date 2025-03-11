#2.class Mwthod and self
# problem:Add a method to the car class that display the full name of the car(brand and model)
class Car:
    def __init__(self,brand ,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"


my_car=Car("Toyota","corolla")    
print(my_car.full_name())