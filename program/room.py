from treasure import Treasure
from monster import Monster


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
        # Returns a tuple With a list of treasure and total value of treasure.
        treasures = Treasure.random_treasure()
        print(f"Tuple of list of treasure and total value of treasure {treasures}.")

    def monster(self):
        # Returns a list of monsters.
        monsters = Monster.random_monster()
        print(f"List of monsters {monsters}.")

    def battle(self):
        pass

    def loose(self):
        pass

    def win(self):
        pass
