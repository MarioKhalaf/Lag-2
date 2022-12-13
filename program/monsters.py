import random


class Monster:
    def __init__(self, name, initiative, endurance, attack, flexibility, probability):
        self.name = name
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.flexibility = flexibility
        self.probability = probability

    def __str__(self):
        return self.name


class GiantSpider(Monster):

    def __init__(self):
        super().__init__("Giant spider", 7, 1, 2, 3, 20)


class Skeleton(Monster):

    def __init__(self):
        super().__init__("Skeleton", 4, 2, 3, 3, 15)


class Orc(Monster):

    def __init__(self):
        super().__init__("Orc", 6, 3, 4, 4, 10)


class Troll(Monster):

    def __init__(self):
        super().__init__("Troll", 2, 4, 7, 2, 5)


def random_monster():
    monster_list = [Orc(), GiantSpider(), Skeleton(), Troll()]
    random_monsters = []
    for monster in monster_list:
        if random.randint(0, 100) <= monster.probability:
            random_monsters.append(monster.name)

    print(random_monsters)


issubclass
