# Temperature converter

unit = input("Is Temperature in Celsius or Fahrenheit (C/F): ")

if unit in ("F", "C") :
    temp = float(input("Enter the Temperature: "))
    
    if unit == "C" :
        temp = round((9 * temp) / 5 + 32, 1)
        print(f"Temperature in Fahrenheit is {temp} F")

    else :
        temp = round((temp - 32) * 5 / 9, 1)
        print(f"Temperature in Celsius is {temp} C")
    
else :
    print(f"{unit} is an invalid unit of measurement")
