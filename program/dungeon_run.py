import json
from room import Room

class Player:

    def __init__(self) -> None:
        self.player = {}
    
    def __str__(self) -> str:
        return self.name

    def write_to_json(self, hero_name, hero):
        self.player["Name"] = hero_name
        self.player["Character"] = hero["Hero"]
        self.player["Treasure"] = 0

        with open("program\saved_games.json") as f:
            data = json.load(f)
        data["Players"].append(self.player)
        with open("program\saved_games.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(data, indent=4))

    def check_name(self, hero_name):
        with open("program\saved_games.json") as f:
            data = json.load(f)
        for value in data["Players"]:
            if value["Name"] == hero_name:
                return True
        return False

    def load_existing_account(self):
        account_name = input("Name of your saved account: ").capitalize()
        with open("program\saved_games.json") as f:
            data = json.load(f)
        for i, player in enumerate(data["Players"]):
            if player["Name"] == account_name:  # if name of account is in there, return True
                print(f"\nWelcome back {account_name}")
                return data["Players"][i]
            else:
                return "This account does not exist\n"

    def name_your_hero(self, hero):
        hero_name = input("Choose a name for your hero: ").capitalize()
        if self.check_name(hero_name):
            print("This name already exists.")
        else:
            self.name = hero_name
            character = hero["Hero"]
            print(f"\nHello {hero_name}, You have chosen the {character} ")
            for key, value in hero.items():
                print(f"{key}, {value}")
            self.write_to_json(hero_name, hero)

    def hero_choice(self, choose_hero):
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


class GameMap:
    def __init__(self, size) -> None:
        self.size = size
        self.map = [["[ ]" for _ in range(self.size)] for _ in range(self.size)]

    def room_menu(self):
        for i in self.map:
            print(' '.join(i))

        print("\nChoose the starting place for your hero.\n\n1. corner 1\n2. corner 2\n3. corner 3\n4. corner 4\nQ. Exit\n")
        choice = input('Your choice: ').lower()
        print(f"\nYou will begin the game at corner {choice}\n")

        if choice == "1":
            self.map[0][0] = "[O]"
        elif choice == "2":
            self.map[0][self.size-1] = "[O]"
        elif choice == "3":
            self.map[self.size-1][0] = "[O]"
        elif choice == "4":
            self.map[self.size-1][self.size-1] = "[O]"

        self.path_options()

    def path_options(self):
        while True:
            try:
                for i in self.map:
                    print(' '.join(i))
                option = input("\nChoose where to go\n\n1. Up\n2. Down\n3. Right\n4. Left\n")
                i, j = self.coordinates()
                if option == "1":
                    self.map[i][j] = "[X]"
                    if i-1 < 0:
                        print("\nYou cannot go there")
                        self.map[i][j] = "[O]"
                    else:
                        self.map[i-1][j] = "[O]"

                elif option == "2":
                    self.map[i+1][j] = "[O]"
                    self.map[i][j] = "[X]"

                elif option == "3":
                    
                    self.map[i][j+1] = "[O]"
                    self.map[i][j] = "[X]"
                
                elif option == "4":
                    self.map[i][j] = "[X]"
                    if j-1 < 0:
                        print("\nYou cannot go there")
                        self.map[i][j] = "[O]"
                    else:
                        self.map[i][j-1] = "[O]"

                else:
                    print("Not a valid option.")

            except IndexError:
                print("\nYou cannot go there.")

    def coordinates(self):
        for i, column in enumerate(self.map):
            for j, row in enumerate(column):
                if "O" in row:
                    return i, j

def main_menu():
    p = Player()
    print("Welcome to the dungeon run!\nChoose your option and begin the adventure.\n")
    while True:
        option = input("1. Create a new hero\n2. Load existing hero\n3. Exit\n")

        if option == "1":
            choose_hero = input('Choose your hero.\n1. The knight\n2. The Wizard\n3. The Thief\n')
            hero = p.hero_choice(choose_hero)
            p.name_your_hero(hero)
            size = int(input("\nChoose a map size by entering one of these numbers: 4,5,8: "))
            g = GameMap(size)
            g.room_menu()

        elif option == "2":
            account = p.load_existing_account()
            print(account)
            size = int(input("\nChoose a map size by entering one of these numbers: 4,5,8: "))
            g = GameMap(size)
            g.room_menu()

        elif option == "3":
            exit("Goodbye!")
        else:
            print("Not a valid option.")


def main():
    main_menu()


if __name__ == "__main__":
    main()
