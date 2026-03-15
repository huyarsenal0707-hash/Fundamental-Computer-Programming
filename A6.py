#1
numbers_list = []
while True:
    num = input("Enter a number (press Enter to stop): ")
    if num == "":
        break
    numbers_list.append(int(num))
numbers_list.sort(reverse=True)
top_five = numbers_list[:5]
print("Top five numbers:", top_five)
#2
seasons = ("winter", "spring", "summer", "autumn")
month = int(input("Enter the number of a month (1-12): "))
if month == 12 or month == 1 or month == 2:
    print("The season is:", seasons[0])
elif month >= 3 and month <= 5:
    print("The season is:", seasons[1])
elif month >= 6 and month <= 8:
    print("The season is:", seasons[2])
else:
    print("The season is:", seasons[3])
#3
names = set()
while True:
    name = input("Enter a name (press Enter to stop): ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
print("\nNames entered:", names)
#4 I haven't figured out how to do this yet.
#5
new_list = []
    
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)
    
    return new_list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filtered_list = remove_odds(original_list)

print("Original list:", original_list)
print("List without odd numbers:", filtered_list)



        
