# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age=int(input("enter your age "))

if (age<13):
    print("Child")
elif (age<19):
    print("Teenager")
elif(age<60):
    print("adult")
else:
    print("senior")