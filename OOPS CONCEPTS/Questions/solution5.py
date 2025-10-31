# Polymorphism
#Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.



class car:
    def __init__(self,userbrand,usermodel):
        self.__brand =userbrand
        self.model=usermodel
    def fullname(self):
        return f"{self.___brand} , {self.model}"
    def get_brand(self):
        return self.__brand+" ! "
    def fuel_type(self):
        return "petor or diesel"
    
class Electriccar(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def dispaly(self):
        return f" {self.brand} {self.model} {self.battery_size}"
    def fuel_type(self):
        return "eLectric charge"

my_tesla = Electriccar("Tesela","Model s","75kwh")
# print(my_tesla.__brand) #not work
print(my_tesla.get_brand())

print(my_tesla.fuel_type())
safari=car("Tata","safari")
print(safari.fuel_type())

# print(my_tesla.model)
# print(my_tesla.dispaly())
        

