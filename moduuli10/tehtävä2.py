# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina
# annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo
# luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Elevator:
    def __init__(self, lowest, top):
        self.lowest = lowest
        self.top = top
        self.floor = lowest

    def move(self, destination):
        if destination > self.floor:
            for _ in range(destination - self.floor):
                if self.floor == self.top:
                    return
                else:
                    self.go_up()
        elif destination < self.floor:
            for _ in range(self.floor - destination):
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

        for _ in range(elevators):
            elevator = Elevator(self.lowest_floor, self.top_floor)
            self.elevator_list.append(elevator)

    def move_elevator(self, elevator_num, destination):
        if elevator_num > len(self.elevator_list) or elevator_num <= 0:
            print("Error: The selected elevator does not exist.")
            return
        current_elevator = self.elevator_list[elevator_num - 1]
        print(f"\nYou are in elevator: {elevator_num}")
        current_elevator.move(destination)


building = Building(0, 10, 3)

building.move_elevator(1, 5)
building.move_elevator(2, 7)
building.move_elevator(3, 3)

