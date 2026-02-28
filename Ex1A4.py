numbers_list = []

while True:
    num = input("Enter a number: ")
    if num == "":
        break
    numbers_list.append(int(num))
numbers_list.sort(reverse=True)
print(f"Five greatest numbers: {numbers_list[:5]}")