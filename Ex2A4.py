num = int(input("Enter a number: "))
if num % 1 == 0 and num % num == 0:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")