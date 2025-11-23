# user={"name":"toji","age":22,1:6}
# print(type(user))
# print(user[1])
# print(user["age"])
# print(user["name"])

#CRUD OPERATIONS

# user["opp"]="Gojo" #creating
# print(user) #read
# user[1]="Greatest" #update
# del user[1]
# print(user)

#traversing

# for i in user:
#     print(user[i])
#     #or
# for i in user.values():
#     print(i)

#Dictionary methods
 
#help(dict)
# user.clear()
#.copy why 
# deep copy
# a={1:2,2:4,3:6,4:8,5:10}
# b=a
# b[1]=0
# print(a)

#shalow copy
# b=a.copy()
# b[1]=100000000
# print(a)

# print(a.get(2))
# print(a.items())



#problems
d1={0:2,1:2,2:6,3:8}
d2={4:1,5:3,6:5,7:7}
# d1.update(d2)
# print(d1)
for i in d2:
    d1[i]=d2[i]

print(d1)
