from character import Character, Knight, Wizard, Thief
from player import Player
from game_map import GameMap
import pyfiglet


def create_character():
    player_name = input("Enter your name: ")
    characters = Character.get_characters_list()
    for character in characters:
        print(f"\nName: {character.character_name} \nInitiative {character.initiative} \nEndurance: {character.endurance} \nAttack: {character.attack} \nFlexibility: {character.flexibility} \nSpecial ability: {character.special_ability}")
    choose_hero = input("""
    Choose your hero.
    1. The knight
    2. The Wizard
    3. The Thief
    """)
    if choose_hero == "1":
        print(Knight())
        knight = Knight()
        player = Player(player_name, 0, knight.character_name, knight.initiative, knight.endurance,
                        knight.attack, knight.flexibility, knight.special_ability)
        print(player.player_name, player.character_name)
        return player
    elif choose_hero == "2":
        wizard = Wizard()
        player = Player(player_name, 0, wizard.character_name, wizard.initiative, wizard.endurance,
                        wizard.attack, wizard.flexibility, wizard.special_ability)
        print(player.player_name, player.character_name)
        return player
    elif choose_hero == "3":
        thief = Thief()
        player = Player(player_name, 0, thief.character_name, thief.initiative, thief.endurance,
                        thief.attack, thief.flexibility, thief.special_ability)
        print(player.player_name, player.character_name)
        return player


def main_menu():
    print(pyfiglet.figlet_format("Dungeon run"))
    print("Welcome to the dungeon run!\nChoose your option and begin the adventure.\n")
    while True:
        option = input("""\n
        1. Create a new hero
        2. Load existing hero
        3. Exit
        """)
        if option == "1":
            player = create_character()
            game_map = GameMap()
            game_map.main_room(player)

        elif option == "2":
            pass

        elif option == "3":
            exit("Goodbye!")

        else:
            print("Not a valid option.")


def main():
    main_menu()


if __name__ == "__main__":
    main()
