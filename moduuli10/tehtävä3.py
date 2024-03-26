# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class Elevator:
    def __init__(self, lowest, top, num):
        self.lowest = lowest
        self.top = top
        self.floor = lowest
        self.num = num

    def move(self, target_floor):
        if target_floor > self.floor:
            for _ in range(target_floor - self.floor):
                if self.floor == self.top:
                    return
                else:
                    self.go_up()
        elif target_floor < self.floor:
            for _ in range(self.floor - target_floor):
                if self.floor == self.lowest:
                    return
                else:
                    self.go_down()

    def go_down(self):
        self.floor -= 1
        print(f"You are on floor {self.floor}")

    def go_up(self):
        self.floor += 1
        print(f"You are on floor {self.floor}")


class Building:
    def __init__(self, lowest_floor, top_floor, elevators):
        self.elevator_list = []
        self.lowest_floor = lowest_floor
        self.top_floor = top_floor

        for i in range(elevators):
            elevator = Elevator(self.lowest_floor, self.top_floor, i + 1)
            self.elevator_list.append(elevator)

    def move_elevator(self, elevator_num, target_floor):
        if elevator_num > len(self.elevator_list) or elevator_num <= 0:
            print("Error: The selected elevator does not exist.")
            return
        current_elevator = self.elevator_list[elevator_num - 1]
        print(f"\nYou are in elevator {current_elevator.num}")
        current_elevator.move(target_floor)

    def fire_alarm(self):
        print("\nFire alarm! All elevators are moving to the ground floor.\n")
        for elevator in self.elevator_list:
            elevator.move(self.lowest_floor)
            print(f"Elevator {elevator.num} is now on floor {self.lowest_floor}.\n")


H = Building(0, 5, 4)
H.move_elevator(4, 4)
H.fire_alarm()


