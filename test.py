import random


treasure_list = ["Loose_change", "Money_bag", "Gold_jewelry", "Gemstone", "Small_treasure_chest"]
antal_skatter = random.randint(0, 5)
print(antal_skatter)
random_treasure = random.choices(treasure_list, weights=(40, 20, 15, 10, 5), k=antal_skatter)
print(random_treasure)
