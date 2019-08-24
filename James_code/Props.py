from Spell import *


class Props:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.health = 1
        self.mana = 1


class Wizard(Props):
    def __init__(self, position, velocity):
        Props.__init__(self, position, velocity)
        self.velocity = velocity
        self.health = 100
        self.mana = 100

    def shout(self, string):
        spell = Spell(string)
        spell.decode_incantation(self.position)
        return spell.cast()
