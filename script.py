print("Welcome to my script!")

name = input("Type the name here: ")

pn = input("Type the phone number here: ")

results = input("Type the name or phone number here: ")

if results.isdigit() == False:
    print(pn + " is the phone number")
    exit()

elif results.isdigit() == True:
    print(name + " is the name.")
    













