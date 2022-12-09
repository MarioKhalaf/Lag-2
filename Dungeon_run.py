import json

class Player:

    def __init__(self) -> None:
        self.player = {}

    
    def write_to_json(self,hero_name, hero):
        treasury = 0
        self.player["Name"] = hero_name
        self.player["Character"] = hero
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

def load_existing_account():
    load_account = input("Name of your hero: ")
    with open("saved_games.json") as f:
        data = json.load(f)
    for player in data["Players"]:
        if player["Name"] == load_account:  # if name of account is in there, return True
            for key, value in player.items():
                print(f"{key}, {value}")
        else:
            print("This account does not exist")

p = Player()
def main():
    print("Welcome to the dungeon run!\nChoose your option and begin the adventure.\n")
    while True:
        option = input("1. Create a new hero\n2. Load existing hero\n3. Exit\n")

        if option == "1":
            choose_hero = input('''Choose your hero.\n1. The knight\n2. The Wizard\n3. The Thief''')
            hero = hero_choice(choose_hero)
            while True:
                hero_name = input("Choose a name for your hero: ")
                if p.check_name(hero_name):
                    print("This name already exists.")
                else:
                    print(f"\nHello {hero_name}, You have chosen: ")
                    for key, value in hero.items():
                        print(f"{key}, {value}")
                    p.write_to_json(hero_name, hero)
            
        elif option == "2": 
            load_existing_account()
        elif option == "3":
            exit("Goodbye!")

if __name__ == "__main__":
    main()
