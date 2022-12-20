class Player:

    def __init__(self, player_name, treasure, character_name, initiative, endurance, attack, flexibility, special_ability):
        self.player_name = player_name
        self.treasure = treasure
        self.character_name = character_name
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.flexibility = flexibility
        self.special_ability = special_ability

    def __str__(self):
        return self.player_name, self.treasure, self.character_name, self.initiative, self.endurance
