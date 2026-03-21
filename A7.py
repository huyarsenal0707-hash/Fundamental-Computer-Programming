#1
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
#2
    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
#3
print("\n=== PART 3 ===")

car.current_speed = 60
car.travelled_distance = 2000

car.drive(1.5)

print("Travelled distance after driving:", car.travelled_distance, "km")
#4
import random
for i in range(1, 11):
    max_speed = random.randint(150, 200)
    cars.append(Car(f"ABC-{i}", max_speed))
race_finished = False
hours = 0
while not race_finished:
    hours += 1
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True