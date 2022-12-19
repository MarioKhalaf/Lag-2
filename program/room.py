from treasure import Treasure
from monster import Monster, GiantSpider, Skeleton, Orc, Troll
import json
from time import sleep
import random
from character import Character, Knight, Wizard, Thief


class Room():

    def __init__(self, account) -> None:
        self.account = account
        self.hero_attributes = self.current_hero()
        self.hero = "l"  # self.account["Character"]

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
        if self.account["Character"] == "Knight":
            knight = {
                "initiative": 5,
                "Endurance": 9,
                "Attack": 6,
                "Flexibility": 4,
            }
            return knight
        elif self.account["Character"] == "Wizard":
            wizard = {
                "initiative": 6,
                "Endurance": 4,
                "Attack": 9,
                "Flexibility": 5
            }
            return wizard
        elif self.account["Character"] == "Thief":
            thief = {
                "initiative": 7,
                "Endurance": 5,
                "Attack": 5,
                "Flexibility": 7
            }
            return thief

    def monster(self):
        # Returns a list of monsters.
        monsters = Monster.random_monster()
        print(f"A {', '.join(monsters)} appeared!")
        return monsters

    def first_attack(self, monster):

        if monster == "GiantSpider":
            monster_class = GiantSpider()
            monster_initiative = self.dice(monster_class.initiative)

        elif monster == "Skeleton":
            monster_class = Skeleton()
            monster_initiative = self.dice(monster_class.initiative)

        elif monster == "Orc":
            monster_class = Orc()
            monster_initiative = self.dice(monster_class.initiative)

        elif monster == "Troll":
            monster_class = Troll()
            monster_initiative = self.dice(monster_class.initiative)

        hero_initiative = self.dice(self.hero_attributes["initiative"])
        if hero_initiative > monster_initiative:
            print(f"The {self.hero} gets the first strike!")
        else:
            print(f"The {monster} gets the first strike!")

        self.battle(hero_initiative, monster_initiative, monster_class)

    def battle(self, hero_iniative, monster_initiative, monster_class):

        if hero_iniative > monster_initiative:
            while True:
                sleep(1)
                hero_attack = self.dice(self.hero_attributes["Attack"])
                monster_flex = self.dice(monster_class.flexibility)
                if hero_attack > monster_flex:
                    monster_class.endurance -= 1
                    print(f"The {self.hero} hits the {monster_class.name}!")
                    if monster_class.endurance == 0:
                        print(f"The {monster_class.name} has been defeated!")
                        break
                else:
                    print(f"The {monster_class.name} blocked the attack.")
                monster_attack = self.dice(monster_class.attack)
                hero_flex = self.dice(self.hero_attributes["Flexibility"])
                if monster_attack > hero_flex:
                    self.hero_attributes["Endurance"] -= 1
                    print(f"The {monster_class.name} hits the {self.hero}!")
                    if self.hero_attributes["Endurance"] == 0:
                        print(f"The {self.hero} has been defeated!")
                        break
                else:
                    print(f"The {self.hero} blocked the attack.")
        else:
            while True:
                sleep(1)
                monster_attack = self.dice(monster_class.attack)
                hero_flex = self.dice(self.hero_attributes["Flexibility"])
                if monster_attack > hero_flex:
                    print(f"The {self.hero} blocked the attack.")
                    self.hero_attributes["Endurance"] -= 1
                    if self.hero_attributes["Endurance"] == 0:
                        print(f"The {self.hero} has been defeated!")
                        break
                else:
                    print(f"The {self.hero} blocked the attack.")
                hero_attack = self.dice(self.hero_attributes["Attack"])
                monster_flex = self.dice(monster_class.flexibility)
                if hero_attack > monster_flex:
                    print(f"The {self.hero} hits the {monster_class.name}!")
                    monster_class.endurance -= 1
                    if monster_class.endurance == 0:
                        print(f"The {monster_class.name} has been defeated!")
                        break
                else:
                    print(f"The {monster_class.name} blocked the attack.")

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
                self.first_attack(monster)

        random_treasures_list = self.treasures()
        self.save_treasures(random_treasures_list[1])

    def save_treasures(self, treasures_value):
        with open("program\saved_games.json") as f:
            data = json.load(f)
            for value in data["Players"]:
                if value["Name"] == self.account["Name"]:
                    value["Treasure"] += treasures_value
                    with open("program\saved_games.json", "w") as f:
                        f.write(json.dumps(data, indent=4))


character = Character.get_characters_list()
print(character)
for i in character:
    print(i.name, i.initiative, i.endurance, i.attack, i.flexibility, i.special_ability)
