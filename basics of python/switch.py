choice = int(input("Enter a number (1-3): "))

if choice == 1:
    print("You chose Option One")
elif choice == 2:
    print("You chose Option Two")
elif choice == 3:
    print("You chose Option Three")
else:
    print("Invalid choice")

#2. Using Dictionary Mapping (No Function)

choice = int(input("Enter a number (1-3): "))

switch = {
    1: "You chose Option One",
    2: "You chose Option Two",
    3: "You chose Option Three"
}

print(switch.get(choice, "Invalid choice"))
#  3. Using match-case (Python 3.10+)

choice = input("Enter a color: ")

match choice:
    case "red":
        print("Stop")
    case "green":
        print("Go")
    case "yellow":
        print("Wait")
    case _:
        print("Invalid color")