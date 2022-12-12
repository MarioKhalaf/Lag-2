import json
from tabulate import tabulate


class Player:

    def __init__(self) -> None:
        self.player = {}

    def write_to_json(self, hero_name, hero):
        treasury = 0
        self.player["Name"] = hero_name
        self.player["Character"] = hero["Hero"]
        self.player["Treasury"] = treasury

        with open("saved_games.json") as f:
            data = json.load(f)
        data["Players"].append(self.player)
        with open("saved_games.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(data, indent=4))

    def check_name(self, hero_name):
        with open("saved_games.json") as f:
            data = json.load(f)
        for value in data["Players"]:
            if value["Name"] == hero_name:
                return True
        return False


def hero_choice(choose_hero):
    heroes = [
        {
            "Hero": "Knight",
            "Iniative": 5,
            "Endurance": 9,
            "Attack": 6,
            "Flexibility": 4
        },
        {
            "Hero": "Wizard",
            "Iniative": 6,
            "Endurance": 4,
            "Attack": 9,
            "Flexibility": 5
        },
        {
            "Hero": "Thief",
            "Iniative": 7,
            "Endurance": 5,
            "Attack": 5,
            "Flexibility": 7
        }
    ]

    if choose_hero == "1":
        return heroes[0]

    elif choose_hero == "2":
        return heroes[1]

    elif choose_hero == "3":
        return heroes[2]


def rooms():
    size = int(input("Choose a map size by entering one of these numbers: 4,5,8: "))

    for i in range(size):
        for i in range(size):
            print('X ', end='')
        print()


def room_menu():
    rooms()
    print("\n1. corner 1\n2. corner 2\n3. corner 3\n4. corner 4\nQ. Exit\n")
    choice = input('Your choice: ').lower()
    if choice == "1":
        pass
    print(f"\nYou will begin the game at corner {choice}")


def load_existing_account():
    account_name = input("Name of your saved account: ").capitalize()
    with open("saved_games.json") as f:
        data = json.load(f)
    for i, player in enumerate(data["Players"]):
        if player["Name"] == account_name:  # if name of account is in there, return True
            print(f"\nWelcome back {account_name}")
            return data["Players"][i]
        else:
            print("This account does not exist\n")


p = Player()


def name_your_hero(hero):
    hero_name = input("Choose a name for your hero: ").capitalize()
    if p.check_name(hero_name):
        print("This name already exists.")
    else:
        character = hero["Hero"]
        print(f"\nHello {hero_name}, You have chosen the {character} ")
        for key, value in hero.items():
            print(f"{key}, {value}")
        p.write_to_json(hero_name, hero)
        room_menu()


def main_menu():
    print("Welcome to the dungeon run!\nChoose your option and begin the adventure.\n")
    while True:
        option = input("1. Create a new hero\n2. Load existing hero\n3. Exit\n")

        if option == "1":
            choose_hero = input('Choose your hero.\n1. The knight\n2. The Wizard\n3. The Thief\n')
            hero = hero_choice(choose_hero)
            name_your_hero(hero)

        elif option == "2":
            account = load_existing_account()
            print(account)
        elif option == "3":
            exit("Goodbye!")
        else:
            print("Not a valid option.")


def main():
    main_menu()


if __name__ == "__main__":
    main()
