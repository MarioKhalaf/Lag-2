from program.characters import Characters


class thief(Characters):
    def _init_(self):
        self.Initiative = 7
        self.Endurance = 5
        self.Attack = 5
        self.Flexibility = 7
        # Specialförmåga: Kritisk träff. Tjuven har 25% chans att göra dubbel skada varje gång tjuven attackerar.
        self.Special_ability = "Critical hit"
