#9. Class Inheritance and isinstance() Function
#Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

#8. Property Decorators
#Problem: Use a property decorator in the Car class to make the model attribute read-only.


class car:
    total_car=0
    def __init__(self,userbrand,usermodel):
        self.__brand =userbrand
        self.__model=usermodel
        # self.total_car
        car.total_car +=1
    def fullname(self):
        return f"{self.___brand} , {self.__model}"
    def get_brand(self):
        return self.__brand+" ! "
    @staticmethod
    def general_desc():
        return "cars are need to trasport"
    @property #not allow to change after constructor is created 
    def model(self):
        return self.__model
    
class Electriccar(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def dispaly(self):
        return f" {self.brand} {self.model} {self.battery_size}"

my_tesla = Electriccar("Tesela","Model s","75kwh")

print(isinstance(my_tesla,car))
print(isinstance(my_tesla,car))


        

