
class car:
    def __init__(self,userbrand,usermodel):
        self.brand =userbrand
        self.model=usermodel
    def fullname(self):
        return f"{self.brand} , {self.model}"
        
my_car=car("BWM","2025")
print(my_car.brand)
print(my_car.model)
print(my_car.fullname())
