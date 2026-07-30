#python weight converter

weight = float(input("Enter your weight: "))
unit = input("kilogram or pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your Weight is {round(weight, 2)} {unit}")

elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your Weight is {round(weight, 2)} {unit}")


else :
    print(f"{unit} is not a valid unit")
