#for Loop using range()
for i in range(1,21,1):
    print(i,end=' ')
for i in range(16,0,-1):
    print(i,end="  ")
for i in range(-20,0,1):
    print(i,end="  ")

#lets make an table for user
num =int(input("enter a number "))

for i in range(num,(num*20)+1,num):
    print(i)
for i in range(1,21):
    print(f"{num}*{i} ={num*i}")

    #for loops in string
name =" hello your are coder for python programming"
for i in name:
    print(i,end=" ")

# #using len ()
for i in range(len(name)):
    print(name[i],end=' ')

# #using break statements
for i in range(1,21):
    if i==16:
        break
    print(i,end=" ")

#using continue statement
for i in range(1,21):
    if i ==16:
        continue
    print(i,end=" ")

   #problems for using for loop 
   #problem 1

user =int(input("enter nummber how times to print "))
for i in range(0,user):
    print("helloworld")

#problem 2
#sum of n natural number

num =int(input("enter a number"))
sum=0

for i in range(1,num+1):
    sum+=i
print(sum)

#factorial problem

num =int(input("enter a number"))
fact =1
for i in range(1,num+1):
    fact *=i
print(f"factorial of given number {num} is {fact}")

num = int(input("Enter any  number"))
even,odd=0,0
for i in range(1,num+1,1):
    if i %2 ==0:
       even+=i
    else :
       odd+=i
print(f"sum of odd and even are {even} ,{odd}")

#Print all the factors of a number
num=int(input("enter a number"))
print("factors of given numbers is ")
for i in range(1,num):
    if num%i ==0:
        print(i)
 

# Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself 
# Ex -  6 = 1, 2, 3 = 6
 
num=int(input("enter a number"))
sum=0
print("factors of given numbers is ")
for i in range(1,num):
    if num%i ==0:
        sum +=i
if sum==num:
    print("it is a perfect number")
else:
    print("not an perfect number")

#prime or not
num=int(input("enter a number"))
count=0
print("factors of given numbers is ")
for i in range(1,num):
    if num%i ==0:
        count+=1

if count <=2:
    print("it is a prime number")
else:
    print("not an prime number")

#reverse of string
input=input("enter a string")
for i in range(len(input)-1,-1,-1):
    print(input[i])

#Check string is Pallindrome or not
str1=input("enter a string name")
str2=""
for i in range(len(str1)-1,-1,-1):
    str2 +=str1[i]
if str1==str2:
    print("it is a Pallindrome")
else:
    print("not an Pallindrome")


#Count all letters, digits, and special symbols from a given 
# string 
# Given: str1 = "P@#yn26at^&i5ve" 
# Expected Outcome: 
# Total counts of chars, digits, and symbols 
# Chars = 8 
# Digits = 3 
# Symbol = 4

str1 = "P@#yn26at^&i5ve"
dig=0
char=0
spchar=0 
for i in str1:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        char+=1
    else:
        spchar+=1
print(f"your digits - {dig}\n your character = {char}\n your special character ={spchar}")
 
print(dir(str))