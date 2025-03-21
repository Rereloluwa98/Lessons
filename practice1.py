Name = input("What's your name?")
Age = input("What's your age?")

if int(Name) >= 18:
    print (f"You're welcome!",{Name})
elif int(Name) == 18:
    print("Ok, You're old enough, barely!")
else:
    print("Nope!, too young!")