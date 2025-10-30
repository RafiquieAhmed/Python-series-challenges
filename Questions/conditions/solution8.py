#Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
passcode=input("enter your password")

if len(passcode) <6:
    strength="week"
elif len(passcode) <=10:
    strength ="Medium"
else:
    strength="Strong"
print("password strenght is :",strength)