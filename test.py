import random


#treasure_list = ["Loose_change", "Money_bag", "Gold_jewelry", "Gemstone", "Small_treasure_chest"]
#antal_skatter = random.randint(0, 5)
#print(antal_skatter)
#random_treasure = random.choices(treasure_list, weights=(40, 20, 15, 10, 5), k=5)
#print(random_treasure)

random.randint(0, 100)
if random.randint(0, 100) <= 40:
    print("Loose_change")

random.randint(0, 100)
if random.randint(0, 100) <= 20:
    print("Money_bag")

random.randint(0, 100)
if random.randint(0, 100) <= 15:
    print("Gold_jewelry")

random.randint(0, 100)
if random.randint(0, 100) <= 10:
    print("Gemstone")

random.randint(0, 100)
if random.randint(0, 100) <= 5:
    print("Small_treasure_chest")

# Istället för print kan man lägga till spelkaraktären i en lista och sedan skriva ut listan.