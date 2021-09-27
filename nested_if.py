car = input("What colour is the car, red, blue or yellow? ")
gender = input("Is the driver male or female? ")

if car == "blue":
    if gender == "male":
        print("The driver must be Dean.")
    else:
        print("The driver must be Ellie.")
elif car == "red":
    if gender == "male":
        print("The driver must be Matt.")
    else:
        print("The driver must be Carolina.")
else:
    if gender == "male":
        print("The driver must be Alex.")
    else:
        print("The driver must be Kirsty.")
