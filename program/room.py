from treasure import Treasure
from monsters import Monsters


class Room():

    def __init__(self) -> None:
        self.visited = False
        self.coordinate = ()
        self.monster = False

    def wall(self):
        pass

    def door(self):
        pass

    def treasures(self):
        # if self.monster = False
        list_of_treasures = Treasure.random_treasure2()
        print(f"Antal skatter {list_of_treasures}.")
        number_of_points = Treasure.calculate_points(list_of_treasures)
        print(f"Antal poäng {number_of_points}.")

    def monster(self):
        list_of_monsters = Monsters.random_monster()
        print(f"Antal skatter {list_of_monsters}.")

    def battle(self):
        pass

    def loose(self):
        pass

    def win(self):
        pass
