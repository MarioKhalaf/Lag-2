import json


def hero_choice(choose_hero):
    heroes = [
        {
            "Hero": "Knight",
            "Iniative": 5,
            "Endurance": 9,
            "Attack": 6,
            "Flexibility": 4
        },
        {"Hero": "Wizard",
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

def load_existing_account():
    load_account = input("Name of your hero: ")
    with open("saved_games.json") as f:
        data = json.load(f)
    for player in data["Players"]:
        if player["Name"] == load_account:  # if name of account is in there, return True
            for key, value in player.items():
                print(f"{key}, {value}")
        print("There is no such player saved.")

def main():
    option = input('''
Welcome to the dungeon run!
Choose your option and begin the adventure.

1. Create a new hero
2. Load existing hero

''')
    if option == "1":
        choose_hero = input('''
Choose your hero.

1. The knight
2. The Wizard
3. The Thief
''')
        hero = hero_choice(choose_hero)
        hero_name = input("Choose a name for your hero: ")
        print(f"\nHello {hero_name}, You have chosen: ")
        for key, value in hero.items():
            print(f"{key}, {value}")

        treasury = 0
        player = {}
        player["Name"] = hero_name
        player["Character"] = hero
        player["Treasury"] = treasury

        with open("saved_games.json") as f:
            data = json.load(f)
        data["Players"].append(player)  # Appends to end of accounts list inside file
        with open("saved_games.json", "w", encoding="utf-8") as f:  # write back updated file
            f.write(json.dumps(data, indent=4))

    elif option == "2":
       load_existing_account()


if __name__ == "__main__":
    main()
