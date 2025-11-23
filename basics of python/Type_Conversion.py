# Implicit Type Conversion
a=10
b=2.0
c=10+2j
print(a+b)
print(a+c)

print(True+14) # true =1
print(False+7) # false =0


#explicit Type conversion
a=10
b="hello"
a=str(a)
print(a+b) #str

#str->int
a=20
b=int("40")
print(a+b)

#float ->int
a=2.0
b=6
c=int(b/a)
print(c)








