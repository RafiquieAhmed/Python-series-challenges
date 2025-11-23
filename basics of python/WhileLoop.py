#Separate each digit of a number and print it on the new line
# num =int(input("enter a number"))
# while (num>0):
#     print(num%10)
#     num//=10

#Accept a number and print its reverse
# num =int(input("enter a number "))
# rev =0
# while (num>0):
#     rev=rev*10+num%10
#     num//=10
# print(rev)
    
#Accept a number and check if it is a pallindromic number (If number and its reverse are equal

# num=int(input("Enter a Number"))
# temp=num
# rev=0

# while(num>0):
#     rev=rev*10+num%10
#     num//=10

# if temp==rev:
#     print(" It is an pallindromic number")
# else:
#     print("It is not pallindromic number")

#reate a random number guessing game with python.

import random

num=random.randint(1,100)
tries=0
while True :
    guess=int(input("ENter a guessing number between 1 -100"))
    if guess==num:
        tries+=1
        print(f"Your gessing is correct {num},your take chances of {tries}")
        break
    elif num<guess:
        tries+=1
        print("your number is  less than your guess")
    elif num>guess:
        tries+=1
        print("your number is more than your guess")

    else:
        tries+=1
        print(f"sorry your guessing number is wrong {guess},")
