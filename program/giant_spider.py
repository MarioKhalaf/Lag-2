from program.monsters import Monsters


class Giant_spider(Monsters):
    def _init_(self):
        self.Initiative = 7
        self.Endurance = 1
        self.Attack = 2
        self.Flexibility = 3
        self.probability = "20%"
