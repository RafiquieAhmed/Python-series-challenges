age=int (input("enter your age : "))
#try:
if age<10 or age>18 :
        raise ValueError("your age is not matched for this program (10-18)")
else:
        print("your enrolled for this program")
# except Exception as err:
#     print(f"error has occured {err}")
print("your selected")