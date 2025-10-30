#Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
pet=(input("enter you pet species"))
age=int(input("pet age : "))

if (pet =="Dog" and age<2):
    food = "Puppy"
elif (pet =="Cat" and age >5):
    food = "senior cat "

print("Your pet is {}, age is {}, food recommended is {}.".format(pet, age, food))

