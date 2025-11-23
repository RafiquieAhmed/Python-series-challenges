#. Arithmetic Operators
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)

#comaparsion operation 
print(a<b)
print(a>b)
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)

# Assignment Operators
x=10
x+=3
print(x)
x-=3
print(x)
x*=3
print(x)
x/=3
print(x)
x%=3
print(x)
x**=3
print(x)
x//=3
print(x)

#logical operator
x= 10
print(x<30 and x>9)
print(x and  x<2) # only T | T= T
print(x>12 or x==19) # only F | F = F
print(not x!=10) # T->F or F->T

#  5. Identity Operators
a=[1,2,3,4,5]
b=a
print(a is b)
b=5
print(a is b)

a=[1,2,3]
b=[1,2,4]
print(a is not b)

# 6 Membership Operators
a=["hello","new","world","!"]
print("hellos"in a)
print("hellos" not in a)

#membership operator
