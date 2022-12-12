from program.characters import Characters


class wizard(Characters):
    def _init_(self):
        self.Initiative = 6
        self.Endurance = 4
        self.Attack = 9
        self.Flexibility = 5
        # Specialförmåga: Ljussken. Trollkarlen kan göra monster blinda och har därför alltid 80% chans att fly från strider.
        self.Special_ability = "Shining light"
