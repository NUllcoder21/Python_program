#3.inheritance
#problem:create an ElectricCar class that inherits from the car class and hs an additional attributes battery_size
class Car:
    def __init__(self,brand ,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
    def full_name2(self):
        return f"{self.brand} {self.model} {self.battery_size}"

my_tesla = ElectricCar("Tesla","Model s","85kwh")
print(my_tesla.full_name2())
my_car=Car("Toyota","corolla")    
print(my_car.full_name())