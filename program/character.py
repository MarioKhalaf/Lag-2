class Character:
    def __init__(self, name, initiative, endurance, attack, flexibility, special_ability):
        self.name = name
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.flexibility = flexibility
        self.special_ability = special_ability

    def __str__(self):
        return self.name

    def get_characters_list():
        list = [Knight(), Wizard(), Thief()]
        return list


class Knight(Character):

    def __init__(self):
        # Riddaren blockerar alltid första attacken per strid med sin sköld, och behöver därför varken undvika eller ta någon skada.
        super().__init__("Knight", 5, 9, 6, 4, "Shield block")


class Wizard(Character):

    def __init__(self):
        # Specialförmåga: Ljussken. Trollkarlen kan göra monster blinda och har därför alltid 80% chans att fly från strider.
        super().__init__("Wizard", 6, 4, 9, 5, "Shining light")


class Thief(Character):

    def __init__(self):
        # Specialförmåga: Kritisk träff. Tjuven har 25% chans att göra dubbel skada varje gång tjuven attackerar.
        super().__init__("Thief", 7, 5, 5, 7, "Critical hit")
