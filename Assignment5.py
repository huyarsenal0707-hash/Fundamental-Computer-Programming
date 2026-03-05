#1 
import re
course = str(input("Enter a course code: "))
pattern = r'^[A-Z]{2,3}\d{3}$'
if re.match(pattern, course):
    print("True")
else:
    print("False")

#2
import re 
hex_color = str(input("Enter a hex color code: "))
pattern = r'^#([A-Fa-f0-9]{6}$)'
if re.match(pattern, hex_color):
    print("True")
else:
    print("False")

#3
import re
import math
sentence = str(input("Enter whatever you want: "))
match = re.findall(r"\d+", sentence)
total = 0
if match:
    for num in match:
        total += int(num)
    print("The sum of the numbers in the sentence is:", total)
    
else:
    print("No numbers found in the sentence.")
    
#4
import re
string = str(input("Your phone number: "))
pattern = r'\+84\d+|\b\d{10}\b'
if re.match(pattern, string):
    print(re.sub(r'\+84\d+|\b\d{10}\b', '{REDACTED}', string))
else:
    print("Invalid phone number format.")
#5
import random
points = int(input("Enter the number of points: "))
inside = 0
for i in range(points):
    x= random.uniform(-1, 1)
    y= random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        inside += 1
pi =    (inside / points) * 4
print("Estimated value of pi:", pi)



