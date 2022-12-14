from treasure import Treasure
from monster import Monster
import json


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

    def main(self):

        treasures_value = Room.treasures()
        treasures_value = treasures_value[1]
        print(treasures_value)

        with open("saved_games.json") as f:
            data = json.load(f)
            for value in data["Players"]:
                if value["Name"] == Player.__str__:
                    value["Treasure"] += treasures_value
                    with open("saved_games.json", "w", encoding="utf-8") as f:
                        f.write(json.dumps(data, indent=4))
