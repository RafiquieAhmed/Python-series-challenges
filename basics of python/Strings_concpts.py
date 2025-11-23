 #string Concpts

print(chr(128522))

#methods

# indexing

value="I am learning python now"
 # postive indexing

"""PYTHON
   012345 """
print(value[0])
print(value[1])

#negitive ndexing
""" PYTHON
    -6-5-4-3-2-1"""

print(value[-1])
print(value[-7])

#slicing
print(value[5:])#using start only
print(value[:-4]) #using stop only
print(value[::5]) #using step only

#Concatenation
cat1="py_"
cat2="version 3.0"
print(cat1+cat2)


# Repetition

print("yohoho " *3)

# common methods
#upper ()
name=" sanji know respect food and ladies"
print(name.upper())

#lower()
loyality="NOTHING HAPPEND MOVEMENT"
print(loyality.lower())

print(loyality.split())
print(loyality.strip())

#looping 
for i in loyality[0:-9:1]:
    print(i)

#length ()

print(len(loyality))

#String Formatting

qus="What are you doing ?"
print(f"{qus} {value}")
name = "Alice"
print(f"Hello, {name}")

