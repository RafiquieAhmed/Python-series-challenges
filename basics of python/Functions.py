def say_hi():
    """This function prints a simple greeting"""
    print("Hi!")

print(say_hi.__doc__)

# def pallindrome(str):
#     rev=""
#     for i in range(len(str)-1,-1,-1):
#         rev=rev+str[i]
    
#     if rev==str:
#         print("pallindrome")
#     else :
#         print("not pallidrome")
# pallindrome("LOL")
# pallindrome("knvirn")

#using return keyword

def calling():
    return "calling some one"

print(calling())
