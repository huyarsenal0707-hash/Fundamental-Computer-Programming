import random
three_digit_combination = [random.randint(0, 9) for _ in range(3)]
four_digit_combination = [random.randint(1, 6) for _ in range(4)]
print(''.join(map(str, three_digit_combination)))
print(''.join(map(str, four_digit_combination)))