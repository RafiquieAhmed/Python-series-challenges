# coditional statements
#if

# marks=int(input("Enter yours for results"))
# if marks>50:
#     print(f"congrulation your pass, your scored {marks}")

# #using if-else statements
# age=int(input("please enter your age"))
# if age > 18:
#     print("your adult")

# else :
#     print("your not an adult")

#elif-statements

# Anime=input("please enter which you want vote")
# if Anime=="DBZ":
#     print("vote for Goku")
# elif Anime=="One pice":
#     print("vote Luffy")
# elif Anime =="Naruto":
#     print("vote for Naruto")
# elif Anime =='Bleach':
#     print("vote for itcho")
# else:
#     print("Note avilable for vote")

    #nested if 

# Anime=input("please enter which you want vote")
# name=["Gohan","Goten","vegeta","trunks"]
# if Anime=="DBZ":
#     print("vote for Goku")
#     char_name =input("charcter name")
#     if char_name in name :
#         print(f"slected charcater is {char_name}")
# elif Anime=="One pice":
#     print("vote Luffy")
# elif Anime =="Naruto":
#     print("vote for Naruto")
# elif Anime =='Bleach':
#     print("vote for itcho")
# else:
#     print("Note avilable for vote")

    #problems 1
   # find of greater of two numbers
# num1,num2=map(int,input("enter any two number").split())
# if num1>num2:
#     print(f"{num1} greater than {num2}")
# elif num1<num2 :
#     print(f"{num1} is less than {num2}")
# else:
#     print("both are equal")

# problem 2

# gender =input("please enter the gender based on { M -Male , F- Female}")
# if gender =='M' or gender =='m':
#     print("Good moring Sir")
# elif gender =='F' or gender=='f':
#     print("Good morining Mam")
# else :
#     print("invaild gender")

#problem 3

# num=int(input("enter any number to check odd or even"))
# if num%2==0:
#     print("even Nuber")
# else:
#     print("Odd number")

# problem 4

year=int(input("enter a year number"))

if year %100 ==0 and year % 400==0:
    print("it leaap year")
elif year %100 !=0 and year %4 == 0:
    print("leap year")
else:
    print("not a leap year")

 