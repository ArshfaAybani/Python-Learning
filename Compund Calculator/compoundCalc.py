#Python compund interest calculator

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter your principal amount: ")) 
    if principal <= 0:
        print(f"Your principal amount {principal} should be more than 0")

while rate <= 0:
    rate = float(input("Enter your rate amount: "))
    if rate <= 0:
        print(f"Your rate of interest {rate} should be more than 0")


while time <= 0:
    time = int(input("Enter your time(in yrs) amount: "))
    if time <= 0:
        print(f"Your time(in yrs) {time} should be more than 0")

total = principal * pow(1 + (rate / 100), time)
print(f"Your Balance after {time} years is {total}")
