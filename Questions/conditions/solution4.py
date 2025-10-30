#Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
fruit ="Banana"


user_input=input("enter which color the banana: ")

if fruit=="Banana":
    if user_input == "Green" or user_input =="green":
        print("Unripe")
    elif user_input == "yellow" or user_input =="Yellow":
        print("Unripe")
    elif user_input =="Brown" or user_input=="Brown":
        print("overripe ")