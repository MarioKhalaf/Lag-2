import random
from dungeon_run import Player


player_health = 10
monster_health = 10


def player_attack():
    # pick the hero
    damage = 9  # detta är bara exempel--->lägga heroes attack
    print(f" The palayer does {damage} points of damage to monster")
    return damage


def monster_attack():
    # pick the monster
    damage = 8  # detta är bara exempel--->lägga monster attack
    print(f" The monster does {damage} points of damage to monster")
    return damage


while player_health > 0 and monster_health > 0:
    monster_health -= player_attack()
    if monster_health <= 0:
        break

    player_health -= monster_attack()
    if player_health > 0:
        print("You won the battle")

    else:
        print("Monster won the battle")
