from treasure import Treasure
from monster import Monster
from character import Knight, Wizard, Thief
import json
from time import sleep
import random


class Room():

    def __init__(self, account) -> None:
        self.account = account
        self.hero = self.account["Character"]
        self.hero_class = self.current_hero()

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

    def dice(self, attribute):
        rolled_value = 0
        for i in range(attribute):
            dice = random.randint(1, 6)
            rolled_value += dice
        return rolled_value

    def current_hero(self):
        knight = Knight()
        wizard = Wizard()
        thief = Thief()
        if self.hero == 'Knight':
            return knight
        elif self.hero == 'Wizard':
            return wizard
        elif self.hero == 'Thief':
            return thief
        

    def monster(self):
        monsters = Monster.random_monster()
        for i in monsters:
            print(f"A {i.name} appeared!")
        return monsters

    def escape(self, monster):
        option = input("Choose an option.\n1. Escape\n2. Attack\n")
        if option == "1":
            print("Returning to previous room...")
        else:
            self.first_attack(monster)
            random_treasures_list = self.treasures()
            self.save_treasures(random_treasures_list[1])

    def first_attack(self, monster):
        monster_initiative = self.dice(monster.initiative)
        hero_initiative = self.dice(self.hero_class.initiative)

        if hero_initiative > monster_initiative:
            print(f"The {self.hero} gets the first strike!")
        else:
            print(f"The {monster} gets the first strike!")

        self.battle(hero_initiative, monster_initiative, monster)

    def battle(self, hero_iniative, monster_initiative, monster):

        if hero_iniative > monster_initiative:
            while True:
                sleep(1)
                hero_attack = self.dice(self.hero_class.attack)
                monster_flex = self.dice(monster.flexibility)
                if hero_attack > monster_flex:
                    monster.endurance -= 1
                    print(f"The {self.hero} hits the {monster.name}!")
                    if monster.endurance == 0:
                        print(f"The {monster.name} has been defeated!")
                        break
                else:
                    print(f"The {monster.name} blocked the attack.")
                monster_attack = self.dice(monster.attack)
                hero_flex = self.dice(self.hero_class.flexibility)
                if monster_attack > hero_flex:
                    self.hero_class.endurance -= 1
                    print(f"The {monster.name} hits the {self.hero}!")
                    if self.hero_class.endurance == 0:
                        print(f"The {self.hero} has been defeated!")
                        print("Game over!")
                        sleep(2)
                        exit("Exiting...")
                else:
                    print(f"The {self.hero} blocked the attack.")
        else:
            while True:
                sleep(1)
                monster_attack = self.dice(monster.attack)
                hero_flex = self.dice(self.hero_class.flexibility)
                if monster_attack > hero_flex:
                    print(f"The {monster.name} hits the {self.hero}!")
                    self.hero_class.endurance -= 1
                    if self.hero_class.endurance == 0:
                        print(f"The {self.hero} has been defeated!")
                        print("Game over!")
                        sleep(2)
                        exit("Exiting...")
                else:
                    print(f"The {self.hero} blocked the attack.")

                hero_attack = self.dice(self.hero_class.attack)
                monster_flex = self.dice(monster.flexibility)
                if hero_attack > monster_flex:
                    print(f"The {self.hero} hits the {monster.name}!")
                    monster.endurance -= 1
                    if monster.endurance == 0:
                        print(f"The {monster.name} has been defeated!")
                        break
                else:
                    print(f"The {monster.name} blocked the attack.")

    def loose(self):
        pass

    def win(self):
        pass

    def main_room1(self):
        print("You are in a room")

    def main_room(self):
        print("You enter a new room")
        sleep(1)
        monster_list = self.monster()
        if len(monster_list) == 0:
            print("No monster in this room")
        else:
            for monster in monster_list:
                self.escape(monster)

    def save_treasures(self, treasures_value):
        with open("program\saved_games.json") as f:
            data = json.load(f)
            for value in data["Players"]:
                if value["Name"] == self.account["Name"]:
                    value["Treasure"] += treasures_value
                    with open("program\saved_games.json", "w") as f:
                        f.write(json.dumps(data, indent=4))
