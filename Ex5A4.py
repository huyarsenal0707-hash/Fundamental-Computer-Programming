numbers_list = []
even_numbers = []
while True:
    number = int(input("Enter a number (press 0 to quit): "))
    if number == 0:
        break
    numbers_list.append(number)
for number in numbers_list:
    if number % 2 == 0:
        even_numbers.append(number)
print(f"Before, {numbers_list} and after, {even_numbers}")
        