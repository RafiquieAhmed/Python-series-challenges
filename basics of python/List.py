# creating list
list=[1,2,3,4,5,7.0,"python"]
list[1]=1 #mutable

print(list)

#List traversing
for i in range(len(list)):
    print(list[i])

    #traversing list using values 
for i in list:
    print(i)
    
    #methods
#    to see the list proprites
# print(dir(list))

#if you want what is the properties of list do then do this
# help(list) # press enter to see more

#append
list.append(6)
print(list)

#using insert
list.insert(1,2)# position,element _value
print(list)
#using extend
list.extend([7,8,9,"3090"])
print(list)

#using remove
list.remove(9)
print(list)
list.clear()
print(list)

#problems
#Print positive and negative elements of an List
# list=[1,-49,39,70,-3,-70]
# for i in list:
#     if i>0:
#         print(i)
# for i in list:
#     if i<0:
#         print(f"negitve numbers{i}")

#Mean of List elements
list=[1,2,3,4,5,6]
sum=0
for i in list:
    sum=sum+i
print(f"mean: {sum/len(list)}")

#Find the greatest element and print its index too
list=[10,20,30,40,50]
lar=list[0]
index=0
for i in range(len(list)):
    if list[i]>lar:
        lar=list[i]
        index=i
print(f"the largest element is {lar}and index is {index} ")

#ind the second greatest element
list=[1,2,3,4,5,6,7,8]
lar=list[0]
lar_2=list[0]
for i in list:
    if i>lar:
        lar_2=lar
        lar=i
    elif i>lar_2:
        lar_2=i
print(lar,lar_2)

#Check if List is sorted or not
list=[1,2,3,4,5]

for i in range(len(list)-1):
    if list[i]<list[i+1]:
        continue
    else:
        print("un sorted list")
        break
else :
    print("sorted list")