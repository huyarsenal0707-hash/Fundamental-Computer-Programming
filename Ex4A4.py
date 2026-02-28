integers = []

while True:
    num = input("Enter an integer (press q to quit): ")
    if num == 'q':
        break
    integers.append(int(num))
start = 0
for thing in integers:
    start = start + thing
    print(thing, start)
print(f"The sum is {start}")