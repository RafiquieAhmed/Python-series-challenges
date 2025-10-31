#1. Basic Class and Object
#Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

# class car:
#     brand =None
#     model =None
# BMW=car()
# print(BMW)

class car:
    def __init__(self,userbrand,usermodel):
        self.brand =userbrand
        self.model=usermodel
        
my_car=car("BWM","2025")
print(my_car.brand)
print(my_car.model)

