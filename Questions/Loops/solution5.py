#Find the First Non-Repeated Character
input_srt=input("enter an input string")
input_srt =input_srt.lower()

for char in input_srt:
    print(char)
    if input_srt.count(char)==1:
        print("char is :",char)
        break
