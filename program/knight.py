from program.characters import Characters


class Knight(Characters):
    def _init_(self):
        self.Initiative = 5
        self.Endurance = 9
        self.Attack = 6
        self.Flexibility = 4
        # Riddaren blockerar alltid första attacken per strid med sin sköld, och behöver därför varken undvika eller ta någon skada.
        self.Special_ability = "Shield block"
