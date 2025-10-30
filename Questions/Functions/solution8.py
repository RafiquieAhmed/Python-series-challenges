#Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

#usages
# def print_kwargs(name,power):
#     print("name :",name,"power:",power)
# print_kwargs(name="Joy Boy",power="sun god")
# print_kwargs(name="Joy Boy",)
# print_kwargs(name="Joy Boy",power="sun god",enemy ="IMU")

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name="Joy Boy",power="sun god")
print_kwargs(name="Joy Boy")
print_kwargs(name="Joy Boy",power="sun god",enemy ="IMU")
