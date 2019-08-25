class Props:
    def __init__(self, velocity):
        self.velocity = velocity
        self.health = 1
        self.mana = 1


class Wizard(Props):
    def __init__(self, velocity=0):
        Props.__init__(self, velocity)
        self.velocity = velocity
        self.health = 100
        self.mana = 100
        self.said = []

    def shout(self, string):
        self.said.append(string)

    def return_speech(self):
        speech = self.said
        self.said = []
        return speech
