#Class Variables
#Problem: Add a class variable to Car that keeps track of the number of cars created.

class car:
    total_car=0
    def __init__(self,userbrand,usermodel):
        self.__brand =userbrand
        self.model=usermodel
        # self.total_car
        car.total_car +=1
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

# print(my_tesla.get_brand())
car("tata","safari")
print(car.total_car)


        

