numbers_list = []
while True:
    num= input("Enter a number (press q to quit): ")
    if num == 'q':
        break
    numbers_list.append(int(num))
numbers_list.sort(reverse=True)
print("Five greatest numbers are: ")

