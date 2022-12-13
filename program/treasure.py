import random


class Treasure:
    def __init__(self, name, value, probability):
        self.name = name
        self.value = value
        self.probability = probability

    def __str__(self):
        return self.name

    def random_treasure():
        treasure_list = [LooseChange(), MoneyBag(), GoldJewelry(), Gemstone(), SmallTreasureChest()]
        random_treasures = []
        treasure_value = 0
        for treasure in treasure_list:
            if random.randint(0, 100) <= treasure.probability:
                random_treasures.append(treasure.name)
                treasure_value += treasure.value
        return (random_treasures, treasure_value)


class LooseChange(Treasure):

    def __init__(self):
        super().__init__("loose change", 2, 40)


class MoneyBag(Treasure):

    def __init__(self):
        super().__init__("Money bag", 2, 20)


class GoldJewelry(Treasure):

    def __init__(self):
        super().__init__("Gold jewelry", 10, 15)


class Gemstone(Treasure):

    def __init__(self):
        super().__init__("Gemstone", 14, 10)


class SmallTreasureChest(Treasure):

    def __init__(self):
        super().__init__("Small treasure chest", 20, 5)
