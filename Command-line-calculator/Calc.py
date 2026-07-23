#python calculator after 1 day of learning python

operator = input("Enter an operator(+ - * /): ")
num1 = float(input("Enter your 1st number:"))
num2 = float(input("Enter your 2nd number:"))

if operator == "+" :
    result = num1 + num2
    print(round(result, 2))
elif operator == "-" :
    result = num1 - num2
    print(round(result, 2))
elif operator == "*" :
    result = num1 * num2
    print(round(result, 2))
elif operator == "/" :
    result = num1 / num2
    print(round(result, 2))
else : 
    print(f"{operator} is not valid operator")
