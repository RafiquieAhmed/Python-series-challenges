username="chai aur code"

# def prints():
#     print(username)
#     username ="arun"
#     print(username)

# prints()

username = "chai aur code"

def prints():
    global username
    print(username)
    username = "arun"
    print(username)

# prints()
x=99
# def fun_1():
#     global x
#     x=88
# fun_1()
# print(x)


# closure 


# def f1():
#     x=70
#     def f2():
#         print(x)
#     return f2
# myresult =f1()
# myresult()

def chaicoder(num):
    def actual(x):
        return x** num
    return actual

f=chaicoder(2)
g=chaicoder(3)

print(f)
print(f(3))
print(g(3))