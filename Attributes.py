class Characters:
    def _init_(self, Initiative, Endurance, Attack, Flexibility, Special_ability):
        self.Initiative = Initiative
        self.Endurance = Endurance
        self.Attak = Attack
        self.Felxibility = Flexibility
        self.Special_ability = Special_ability

    def Knight(self):
        Initiative = 5
        Endurance = 9
        Attack = 6
        Flexibility = 4
        Special_ability = Shield_block # Riddaren blockerar alltid första attacken per strid med sin sköld, och behöver därför varken undvika eller ta någon skada.

    def The_wizard(self):
        Initiative = 6
        Endurance = 4
        Attack = 9
        Flexibility = 5
        Special_ability = Shining_light # Specialförmåga: Ljussken. Trollkarlen kan göra monster blinda och har därför alltid 80% chans att fly från strider.

    def The_thief(self):
        Initiative = 7
        Endurance = 5
        Attack = 5
        Flexibility = 7
        Special_ability = Critical_hit # Specialförmåga: Kritisk träff. Tjuven har 25% chans att göra dubbel skada varje gång tjuven attackerar.


class Monsters:
    def _init_(self, Initiative, Endurance, Attack, Flexibility, Usuality):
        self.Initiative = Initiative
        self.Endurance = Endurance
        self.Attak = Attack
        self.Felxibility = Flexibility
        self.Usuality = Usuality

    def Giant_spider(self):
        Initiative = 7
        Endurance = 1
        Attack = 2
        Flexibility = 3
        Usuality = "20%"

    def Skeleton(self):
        Initiative = 4
        Endurance = 2
        Attack = 3
        Flexibility = 3
        Usuality = "15%"

    def Orc(self):
        Initiative = 6
        Endurance = 3
        Attack = 4
        Flexibility = 4
        Usuality = "10%"

    def Troll(self):
        Initiative = 2
        Endurance = 4
        Attack = 7
        Flexibility = 2
        Usuality = "5%"


class Treasure:
    def _init_(self, Value, Usuality):
        self.Value = Value
        self.Usuality = Usuality

    def Loose_change(self):
        Value = 2
        Usuality = "40%"

    def Money_bag(self):
        Value = 6
        Usuality = "20%"

    def Gold_jewelry(self):
        Value = 10
        Usuality = "15%"

    def Gemstone(self):
        Value = 14
        Usuality = "10%"

    def Small_treasure_chest(self):
        Value = 20
        Usuality = "5%"
