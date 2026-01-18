talents= float(input("Enter talent: "))
pounds= float(input("Enter pound: "))
lots= float(input("Enter lot: "))
totalgrams= (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)
kilograms= totalgrams // 1000
grams= totalgrams % 1000
print(f"The weight in modern units is: {kilograms} kilograms and {grams:.2f} grams")