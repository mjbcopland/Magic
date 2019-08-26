class Props:
    def __init__(self, velocity, health=1):
        self.velocity = velocity
        self.health = health
        self.mana = 1


class Wizard(Props):
    def __init__(self, velocity=0):
        Props.__init__(self, velocity, 100)
        self.velocity = velocity
        self.mana = 100
        self.said = []

    def shout(self, string):
        self.said.append(string)

    def return_speech(self):
        speech = self.said
        self.said = []
        return speech


class Boulder(Props):
    def __init__(self, velocity, health):
        Props.__init__(self, velocity, health)