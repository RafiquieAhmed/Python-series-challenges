#Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather=input("wheater condition")
weather=weather.capitalize()
print(weather)

if weather =="sunny":
    activity ="Go for a walik"
elif weather =="Rainy":
    activity ="Read a book"
elif weather =="Snowy":
    activity ="Build a snowman"
print(activity)