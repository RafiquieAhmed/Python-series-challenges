#Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number =int(input("enter a number between 1 to 10 : "))
    if (1<= number <=10):
        print("thanks") 
        break
    else:
        print("invaild number , retry the chance")
