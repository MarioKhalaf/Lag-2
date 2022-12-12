import random
import numpy


class Treasure:
    def _init_(self):
        self.value
        self.probability

    def Loose_change(self):
        self.value = 2
        self.probability = "40%"

    def Money_bag(self):
        self.value = 6
        self.probability = "20%"

    def Gold_jewelry(self):
        self.value = 10
        self.probability = "15%"

    def Gemstone(self):
        self.value = 14
        self.probability = "10%"

    def Small_treasure_chest(self):
        self.value = 20
        self.probability = "5%"

    def random_treasure(self):  # with replacements, ska ändras till without replacements.
        treasure_list = [self.Loose_change, self.Money_bag, self.Gold_jewelry, self.Gemstone, self.Small_treasure_chest]
        antal_skatter = random.randint(0, 5)
        print(antal_skatter)
        random_treasure = random.choices(treasure_list, weights=(40, 20, 15, 10, 5), k=antal_skatter)
        print(random_treasure)

    def random_treasure2(self):
        treasure_list = [self.Loose_change, self.Money_bag, self.Gold_jewelry, self.Gemstone, self.Small_treasure_chest]
        antal_skatter = random.randint(1, 5)
        print(antal_skatter)
        random_treasure = numpy.random.choice(treasure_list, antal_skatter, replace=False, p=[
            0.40, 0.20, 0.15, 0.10, 0.05, 0.10])
        print(random_treasure)
