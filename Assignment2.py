#1
def  check_zander_size():
    zander_length = float(input("Enter the length of the zander: "))
    
    
    if zander_length < 42:
        print("The zander is undersized and must be released back to the lake.")
        print(f'The fish is {42 - zander_length:.1f} cm below the size limit.')
    else:
        print("The zander meets the size requirement and can be kept.")
check_zander_size()

#2
def cabin_class():
    describe_cabin = str(input("Enter cabin class : "))
    if describe_cabin == "LUX":
        print("upper-deck cabin with a balcony")
    elif describe_cabin == "A":
        print("above the car deck, equipped with a window")
    elif describe_cabin == "B":
        print("windowless cabin above the car deck")
    elif describe_cabin == "C":
        print("windowless cabin below the car deck")
    else:
        print("Invalid cabin class")
cabin_class()
#3
def hemoglobin_value():
    sex = str(input("Enter your sex: "))
    hemoglobin = float(input("Enter your hemoglobin value: "))
    if sex == "male":
        if hemoglobin < 134:
            print("Your hemoglobin is low.")
        elif hemoglobin > 167:
            print("Your hemoglobin is high.")
        else:
            print("Your hemoglobin is normal.")
    elif sex == "female":
        if hemoglobin < 117:
            print("Your hemoglobin is low.")
        elif hemoglobin > 155:
            print("Your hemoglobin is high.")
        else:
            print("Your hemoglobin is normal.")
hemoglobin_value()
#4
def check_leap_year():
    year = int(input("Enter a year: "))

    if year % 400 == 0:
        print(f"{year} is a leap year.")
    elif year % 100 == 0:
        print(f"{year} is not a leap year.")
    elif year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
check_leap_year()
#5
import math

def pizza_unit_price(diameter_cm, price_usd):
    radius_m = (diameter_cm / 100) / 2
    area = math.pi * radius_m ** 2
    return price_usd / area
d1 = float(input("Enter diameter of pizza 1 (cm): "))
p1 = float(input("Enter price of pizza 1 (USD): "))

d2 = float(input("Enter diameter of pizza 2 (cm): "))
p2 = float(input("Enter price of pizza 2 (USD): "))

unit1 = pizza_unit_price(d1, p1)
unit2 = pizza_unit_price(d2, p2)

print(f"Pizza 1 unit price: {unit1:.2f} USD/m²")
print(f"Pizza 2 unit price: {unit2:.2f} USD/m²")

if unit1 < unit2:
    print("Pizza 1 provides better value for money.")
elif unit2 < unit1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas have the same value for money.")