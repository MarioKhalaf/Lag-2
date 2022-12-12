from program.monsters import Monsters


class Skeleton(Monsters):
    def _init_(self):
        self.Initiative = 4
        self.Endurance = 2
        self.Attack = 3
        self.Flexibility = 3
        self.probability = "15%"
