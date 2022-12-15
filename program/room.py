from treasure import Treasure
from monster import Monster
import random
import json


class Room():

    def __init__(self) -> None:
        self.visited = False
        self.coordinate = ()
        #self.monster = False

    def wall(self):
        pass

    def door(self):
        pass

    def treasures(self):
        # if self.monster = False
        # Returns a tuple With a list of treasure and total value of treasure.
        treasures = Treasure.random_treasure()
        print(f"Tuple of list of treasure and total value of treasure {treasures}.")
        return treasures

    def monster(self):
        # Returns a list of monsters.
        monsters = Monster.random_monster()
        print(f"List of monsters {monsters}.")
        return monsters

    def battle(self):
        print("Time to fight. ")

    def loose(self):
        pass

    def roll_dice(self):
        roll_dice = random.randint(1, 6)
        print(f"You rolled {roll_dice}")

    def win(self):
        pass

    def main_room(self, account):
        print(account)
        print(account["Name"])
        print("You have entered a room")
        monster_list = self.monster()
        print(monster_list)
        if monster_list is None:
            print("No monster")
        else:
            for monster in monster_list:
                print(monster)
                self.battle()
        random_treasures_list = self.treasures()
        for treasures in random_treasures_list[0]:
            print(treasures)
        self.save_treasures(random_treasures_list[1], account)
        print("Returning to map")

    def save_treasures(self, treasures_value, account):
        with open("program\saved_games.json") as f:
            data = json.load(f)
            for value in data["Players"]:
                if value["Name"] == account["Name"]:
                    print(account)
                    value["Treasure"] += treasures_value
                    with open("program\saved_games.json", "w", encoding="utf-8") as f:
                        f.write(json.dumps(data, indent=4))
