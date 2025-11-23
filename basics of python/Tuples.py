#crating a tuple
Tup=()
print(type(Tup))

# user=input("enter a  values for tuple")
# Tvalues=tuple(map(str,user.split()))
# print("tuple",Tvalues)
 
Tval=(1,22,4,"jid","eheho",643,638,22,22,33,444,555,11,332)
print(Tval[0:2])

print(Tval.count(22))
print(Tval.index(22))

# Packing
data = (10, 20, 30)

# Unpacking
a, b, c = data
print(a, b, c)
