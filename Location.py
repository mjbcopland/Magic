class Location:
    def __init__(self, position_x, position_y):
        self.position = [position_x, position_y]
        self.spell_effects = []

    def resolve(self):
        return

    def get_information(self):
        return str(self.position) + " , " + str(self.position[1])
