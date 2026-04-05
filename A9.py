#1
def count_non_blank_line(filename):
    count = 0
    with open(filename, "r", encoding='utf-8') as file: 
        for line in file:
            if line.strip():
                count += 1
    return count_non_blank_line(filename)
#2
def find_key_words(filename, key_words):
    line_numbers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file, start=1):
            if key_words in line:
                line_numbers.append(i)
print(i, )
#3
import math
def calculate_average_score(filename):
    total_score = 0
    count = 0
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            name = line[0]
            score = line[1]
            if line:
                name, score = line.split(',')
                total_score += float(score)
                count += 1
    if count == 0:
        return 0 

    return total_score / count
    
            
    
                