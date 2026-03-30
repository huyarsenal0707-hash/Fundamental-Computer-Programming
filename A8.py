class Elevator
     def __init__(self, bottom_floor, top_floor):
          self.bottom_floor = bottom_floor
          self.top_floor = top_floor
          
     def floor_up(self):
          if self.current_floor < self.top_floor:
             self.current_floor += 1
             print(f"Going up to floor {self.current_floor}")
          else:
               print("Already at the top floor.")
          
     def floor_down(self):
          if self.current_floor > self.bottom_floor:
             self.current_floor -= 1
             print(f"Going down to floor {self.current_floor}")
          else:
               print("Already at the bottom floor.")
     def go_to_floor(self, target_floor):
          if target_floor < self.bottom_floor or target_floor > self.top_floor:
               print("Invalid floor.")
          else target_floor > self.bottom_floor or target_floor < self.top_floor:
               while self.current_floor < target_floor:
                    self.floor_up()
               while self.current_floor > target_floor:
                    self.floor_down()
          print(f"Arrived at floor {self.current_floor}\n.")
     def get_current_floor(self):
          return self.current_floor
#2
class Building:
     def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

        self.elevators = []
            Elevator(bottom_floor, top_floor)
            for _ in range(num_elevators)
        

     def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nElevator {elevator_number} going to floor {destination_floor}")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print("Invalid elevator number!")
#3
     def fire_alarm(self):
         for i, elevator in enumerate(self.elevators):
             print(f"\nElevator {i} responding to fire alarm.")
             elevator.go_to_floor(self.bottom_floor)
#4


          
     

   