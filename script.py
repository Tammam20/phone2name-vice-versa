print("Welcome to my script!")

name = input("Type the name here: ")

if name.isalpha() == False:
    print("This field is not designed for phone numbers!!!")
    exit()

pn = input("Type the phone number here: ")

if pn.isdigit() == False:
    print("This field is not designed for names!!!")
    exit()

results = input("Type the name or phone number here: ")

if results != pn and results != name:
    print("It does not equal name or phone number.")
    exit()

elif results.isalpha() == True :
    print(pn + " is the phone number")
    exit()

elif results.isdigit() == True:
    print(name + " is the name.")
    exit()
