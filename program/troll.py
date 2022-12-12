from program.monsters import Monsters


class Troll(Monsters):
    def _init_(self):
        self.Initiative = 2
        self.Endurance = 4
        self.Attack = 7
        self.Flexibility = 2
        self.probability = "5%"
