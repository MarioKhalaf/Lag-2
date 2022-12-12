import random
import numpy


class Treasure:
    def __init__(self, name, value, probability):
        self.name = name
        self.probability = probability
        self.value = value

    def __str__(self):
        return self.name


class LooseChange(Treasure):

    def __init__(self):
        super().__init__("loose change", 2, 0.4)


class MoneyBag(Treasure):

    def __init__(self):
        super().__init__("Money bag", 2, 0.99)


"""
    def Loose_change(cls):
        self.name = "Loose change"
        self.value = 2
        self.probability = "40%"

    def Money_bag(self):
        self.name = "Money bag"
        self.value = 6
        self.probability = "20%"

    def Gold_jewelry(self):
        self.name = "Gold jewelry"
        self.value = 10
        self.probability = "15%"

    def Gemstone(self):
        self.name = "Gemstone"
        self.value = 14
        self.probability = "10%"

    def Small_treasure_chest(self):
        self.name = "Small treasure chest"
        self.value = 20
        self.probability = "5%"
        return self.name
"""
# def random_treasure():  # with replacements, ska ändras till without replacements.
#   treasure_list = [self.Loose_change, self.Money_bag, self.Gold_jewelry, self.Gemstone, self.Small_treasure_chest]
#  antal_skatter = random.randint(0, 5)
# print(antal_skatter)
#random_treasure = random.choices(treasure_list, weights=(40, 20, 15, 10, 5), k=antal_skatter)
# print(random_treasure)
#["Loose_change", "Money_bag", "Gold_jewelry","Gemstone", "Small_treasure_chest", "ingen_skatt"]
#[("Loose_change", 2), ("Money_bag", 6), ("Gold_jewelry", 10),("Gemstone", 14), ("Small_treasure_chest", 20), ("ingen_skatt", 0)]


def random_treasure():
    treasure_list = [2, 6, 10, 14, 20, 0]
    antal_skatter = random.randint(1, 5)
    print(antal_skatter)
    random_treasure = numpy.random.choice(treasure_list, antal_skatter, replace=False, p=[
        0.40, 0.20, 0.15, 0.10, 0.05, 0.10])
    return random_treasure


def calculate_points(count_treasure):
    val = 0
    for i in count_treasure:
        val = i + val
    return val


treasure_list = [LooseChange(), MoneyBag()]
antal_skatter = random.randint(1, 5)
print(antal_skatter)

random_treasures = []
for treasure in treasure_list:
    if random.randint(0, 100) <= treasure.probability*100:
        random_treasures.append(treasure)

print(random_treasures)
