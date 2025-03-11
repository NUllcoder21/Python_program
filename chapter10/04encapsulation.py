#4.Incapsulation 
# problem: modified the car class to encapsulate the brand attribute ,making it private and provide a getter
class Car:
    def __init__(self,brand ,model):
        self.__brand=brand
        self.model=model

    def get_brand(self):
        return self.__brand + " !"    
    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
    def full_name2(self):
        return f"{self.__brand} {self.model} {self.battery_size}"

my_tesla = ElectricCar("Tesla","Model s","85kwh")
print(my_tesla.full_name2())
print(my_tesla.get_brand())
my_car=Car("Toyota","corolla")    
print(my_car.full_name())