import random
import numpy


class Monsters:

    def __init__(self):
        pass

    def Initiative(self):
        return self.Initiative()

    def Endurance(self):
        return self.Endurance()

    def Attack(self):
        return self.Attack()

    def Flexibility(self):
        return self.Flexibility()

    def probability(self):
        return self.probability()

    def random_monster():
        monster_list = ["giant_spider", "skeleton", "orc", "troll", "no_monster"]
        number_of_monster = random.randint(1, 4)
        print(number_of_monster)
        random_monster = numpy.random.choice(monster_list, number_of_monster, replace=False, p=[
            0.20, 0.15, 0.10, 0.05, 0.50])
        return random_monster
