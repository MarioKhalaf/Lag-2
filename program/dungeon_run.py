import json
from tabulate import tabulate
from time import sleep
from room import Room
import pyfiglet
from character import Character, Knight, Wizard, Thief


class Player:

    def __init__(self) -> None:
        self.player = {}

    def write_to_json(self, hero_name, hero):
        self.player["Name"] = hero_name
        self.player["Character"] = hero
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

    def name_your_hero(self, hero):
        hero_name = input("Choose a name for your hero: ").capitalize()
        if self.check_name(hero_name):
            print("This name already exists.")
        else:
            print(f"\nHello {hero_name}, You have chosen the {hero} ")
            self.write_to_json(hero_name, hero)
            return self.player

    def hero_choice(self):
        choose_hero = input('Choose your hero.\n1. The knight\n2. The Wizard\n3. The Thief\n')
        if choose_hero == "1":
            return "Knight"

        elif choose_hero == "2":
            return "Wizard"

        elif choose_hero == "3":
            return "Thief"

    def create_hero(self):
        hero = self.hero_choice()
        account = self.name_your_hero(hero)
        size = input("\nChoose a map size by entering one of these numbers: 4,5,8: ")
        if size == "4" or size == "5" or size == "8":
            game_map = GameMap(account, int(size))
            game_map.room_menu()
        else:
            print("This is not an option!")


class GameMap:
    def __init__(self, account, size):
        self.account = account
        self.size = size
        self.map = [["[ ]" for _ in range(self.size)] for _ in range(self.size)]

    def room_menu(self):
        size = input("\nChoose a map size by entering one of these numbers: 4,5,8: ")
        if size == "4" or size == "5" or size == "8":
            game_map = GameMap(account, int(size))
            game_map.room_menu()
        else:
            print("This is not an option!")

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
                i, j = self.coordinates()

                option = input("\nChoose where to go\n\n1. Up\n2. Down\n3. Right\n4. Left\n")
                if i == 0 and j == 3:
                    print("You found a room with the exit!")
                    choice = input("""Make your choice:
                                1. Quit the game
                                2. Go to another room
                                """)
                    if choice == "1":
                        self.exit_game()
                        break
                    elif choice == "2":
                        self.map[i+1][j] = "[O]"
                        self.map[i][j] = "[X]"

                elif option == "1":
                    if i-1 < 0:
                        print("\nYou cannot go there\n")
                    else:
                        if "X" in self.map[i-1][j]:
                            print("\nYou have already been in this room\n")
                        else:
                            room = Room(self.account)
                            room.main_room()
                        self.map[i-1][j] = "[O]"
                        self.map[i][j] = "[X]"

                elif option == "2":
                    if "X" in self.map[i+1][j]:
                        print("\nYou have already been in this room\n")
                    else:
                        room = Room(self.account)
                        room.main_room()
                    self.map[i+1][j] = "[O]"
                    self.map[i][j] = "[X]"

                elif option == "3":
                    if "X" in self.map[i][j+1]:
                        print("\nYou have already been in this room\n")
                    else:
                        room = Room(self.account)
                        room.main_room()
                    self.map[i][j+1] = "[O]"
                    self.map[i][j] = "[X]"

                elif option == "4":
                    if j-1 < 0:
                        print("\nYou cannot go there\n")
                    else:
                        if "X" in self.map[i][j-1]:
                            print("\nYou have already been in this room\n")
                        else:
                            room = Room(self.account)
                            room.main_room()
                        self.map[i][j-1] = "[O]"
                        self.map[i][j] = "[X]"

                else:
                    print("Not a valid option.")

            except IndexError:
                print("\nYou cannot go there.\n")

    def navigate_mat(self, x, y):
        if j-1 < 0:
            print("\nYou cannot go there\n")
        else:
            if "X" in self.map[i+x][j+y]:
                print("\nYou have already been in this room\n")
            else:
                room = Room(self.account)
                room.main_room()
            self.map[i+x][j+y] = "[O]"
            self.map[i][j] = "[X]"

    def coordinates(self):
        for i, column in enumerate(self.map):
            for j, row in enumerate(column):
                if "O" in row:
                    return i, j

    def exit_game(self):
        print("\nYou have found the exit!\n")
        with open("program\saved_games.json") as f:
            data = json.load(f)
        for i, player in enumerate(data["Players"]):
            if player["Name"] == self.account["Name"]:
                data["Players"][i]["Treasure"] = self.account["Treasure"]
            with open("program\saved_games.json", "w") as f:
                f.write(json.dumps(data, indent=4))


def load_existing_account():
    with open("program\saved_games.json") as f:
        data = json.load(f)
    header = data["Players"][0].keys()
    rows = [x.values() for x in data["Players"]]
    print(tabulate(rows, header, tablefmt='fancy_grid'))

    account_name = input("Name of your saved account: ").capitalize()
    for i, player in enumerate(data["Players"]):
        if player["Name"] == account_name:
            print(f"\nWelcome back {account_name}")
            return data["Players"][i]


def main_menu():
    print(pyfiglet.figlet_format("Dungeon run"))
    print("Welcome to the dungeon run!\nChoose your option and begin the adventure.\n")
    while True:
        option = input("1. Create a new hero\n2. Load existing hero\n3. Exit\n")
        if option == "1":
            player_name = input(enter your)
            choose_hero = input('Choose your hero.\n1. The knight\n2. The Wizard\n3. The Thief\n')
            characters = Character.get_characters_list()
            for i in characters:
                print(f"Name: {i.name}\n, Initiative {i.initiative}\n, Endurance: {i.endurance}, Attack: {i.attack}, Flexibility: {i.flexibility}, Special ability: {i.special_ability}")

            if choose_hero == "1":
                return Knight()

            elif choose_hero == "2":
                return Wizard()

            elif choose_hero == "3":
                return Thief()

        elif option == "2":
            account = load_existing_account()
            if account is None:
                print("\nThere is no account by that name.\n")
            else:
                size = input("\nChoose a map size by entering one of these numbers: 4,5,8: ")
                if size == "4" or size == "5" or size == "8":
                    game_map = GameMap(account, int(size))
                    game_map.room_menu()
                else:
                    print("This is not an option!")

        elif option == "3":
            exit("Goodbye!")
        else:
            print("Not a valid option.")


def main():
    main_menu()


if __name__ == "__main__":
    main()
