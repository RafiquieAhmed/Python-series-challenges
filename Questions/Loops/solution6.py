#Problem: Compute the factorial of a number using a while loop.
number =int(input("enter a number for factorial"))
factorial =1
while number>1:
    factorial *=number
    number -=1

print("factorial of given number is :",factorial)