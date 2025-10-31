#10. Multiple Inheritance
#Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

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
    
class Battery:
    def Battery_info(self):
        return "this battery"
class Engine:
    def Engine_ingo(self):
        return "heart of car"

class Electriccar(Battery,Engine,car):
    pass

new_car=Electriccar("tesala","Model s")
print(new_car.Engine_ingo())
print(new_car.Battery_info())
