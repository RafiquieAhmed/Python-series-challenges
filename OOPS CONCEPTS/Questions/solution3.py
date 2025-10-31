# Inheritance
#Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class car:
    def __init__(self,userbrand,usermodel):
        self.brand =userbrand
        self.model=usermodel
    def fullname(self):
        return f"{self.brand} , {self.model}"
    
class Electriccar(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def dispaly(self):
        return f"{self.battery_size} {self.brand} {self.model}"

my_tesla = Electriccar("Tesela","Model s","75kwh")


print(my_tesla.dispaly())
        
my_car=car("BWM","2025")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullname())
