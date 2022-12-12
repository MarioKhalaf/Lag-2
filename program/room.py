from treasure import Treasure


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
        treasure = Treasure.random_treasure2()
        points = Treasure.calculate_points()

    def monster(self):
        self.monster = False

    def battle(self):
        pass

    def loose(self):
        pass

    def win(self):
        pass


treasure = Treasure.random_treasure2()
points = Treasure.calculate_points(treasure)
