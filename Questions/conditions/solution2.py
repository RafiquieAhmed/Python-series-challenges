#Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
import datetime
age=int(input("Enter your age:"))

day =datetime.datetime.now().strftime("%A")
price=12 if age >=18 else 8

if "Wednesday" == day:
    price=price -2
    print("ticket price for you is $",price)
else:
    print("ticket price for you is $",price)


