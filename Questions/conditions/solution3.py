#Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score =int(input("enter your marks"))
if score >100:
    print("verfiy your enter marks is invailed enter")
exit()

if score >=90 and score<=100:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("Fail")
