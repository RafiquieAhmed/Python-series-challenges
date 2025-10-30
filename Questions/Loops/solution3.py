#Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
number =int(input("enter a number for table"))

for i in range(1,11):
    if i==5:
        continue
    else:
        print("number *",i ,"=",number*i)
    
