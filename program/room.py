from treasure import Treasure
from monster import Monster
import json
from time import sleep


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
        print(f"You have found {', '.join(treasures[0])} worth {treasures[1]} points.")
        return treasures

    def monster(self):
        # Returns a list of monsters.
        monsters = Monster.random_monster()
        print(f"List of monsters {monsters}.")
        return monsters

    def battle(self):
        pass

    def loose(self):
        pass

    def win(self):
        pass

    def main_room1(self):
        print("You are in a room")

    def main_room(self, account):
        print("You enter a new room")
        sleep(1)
        monster_list = self.monster()
        if len(monster_list) == 0:
            print("No monster in this room")
        else:
            for monster in monster_list:
                # self.battle()
                print(monster)
        random_treasures_list = self.treasures()
        self.save_treasures(random_treasures_list[1], account)
        print("Returning to map")

    def save_treasures(self, treasures_value, account):
        with open("program\saved_games.json") as f:
            data = json.load(f)
            for value in data["Players"]:
                if value["Name"] == account["Name"]:
                    print(account)
                    value["Treasure"] += treasures_value
                    with open("program\saved_games.json", "w") as f:
                        f.write(json.dumps(data, indent=4))
