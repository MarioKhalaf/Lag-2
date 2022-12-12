from program.monsters import Monsters


class Orc(Monsters):
    def _init_(self):
        self.Initiative = 6
        self.Endurance = 3
        self.Attack = 4
        self.Flexibility = 4
        self.probability = "10%"
