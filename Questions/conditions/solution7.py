#Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order=input("enter your coffee order size :")
order=order.capitalize()
order_size=["Small", "Medium","Large" ]
extra_shot =True 
if order in order_size:
    if extra_shot:
        coffee= order +"coffee with an extra shot"
else:
    coffee=order+" Coffee"

print("order: ",coffee)