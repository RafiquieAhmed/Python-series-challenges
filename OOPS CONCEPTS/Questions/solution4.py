#4. Encapsulation
#Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

# Inheritance
#Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class car:
    def __init__(self,userbrand,usermodel):
        self.__brand =userbrand
        self.model=usermodel
    def fullname(self):
        return f"{self.___brand} , {self.model}"
    def get_brand(self):
        return self.__brand+" ! "
    
class Electriccar(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def dispaly(self):
        return f" {self.brand} {self.model} {self.battery_size}"

my_tesla = Electriccar("Tesela","Model s","75kwh")
# print(my_tesla.__brand) #not work
print(my_tesla.get_brand())

# print(my_tesla.model)
# print(my_tesla.dispaly())
        

