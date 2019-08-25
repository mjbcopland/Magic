class Props:
    def __init__(self, velocity):
        self.velocity = velocity
        self.health = 1
        self.mana = 1


class Wizard(Props):
    def __init__(self, velocity):
        Props.__init__(self, velocity)
        self.velocity = velocity
        self.health = 100
        self.mana = 100
        self.said = []

    def shout(self, string):
        return self.said.append(string)

    def return_speech_log(self):
        speech_log = self.said
        self.said = []
        return speech_log
