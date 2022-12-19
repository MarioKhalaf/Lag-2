from treasure import Treasure
from monster import Monster
import json
from time import sleep
import random


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
        print(f"List of monsters {monsters.name}, initiative {monsters.initiative}")
        return monsters

    def battle(self, monster):
        print("start battle")
        print(f"Hi {monster.name}, my initiative is {monster.initiative}")

    def loose(self):
        pass

    def roll_dice(self):
        roll = random.randint(1, 6)
        print(f"You rolled {roll}")
        return roll

    def win(self):
        pass

    def main_room(self, account):
        print("You enter a new room")
        sleep(1)
        monster_list = self.monster()
        if len(monster_list) == 0:
            print("No monster in this room")
        else:
            for monster in monster_list:
                self.battle(monster)
                print(monster)
                print("monster namn", monster.name)
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


monsters = Monster.random_monster()
for i in monsters:
    print(f"Monster: {i.name} attack: {i.attack} initiative: {i.initiative}")
