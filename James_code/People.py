from Spell import *


class Wizard():
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.health = 100
        self.mana = 100

    def shout(self, string):
        spell = Spell(string)
        spell.decode_incantation(self.position)
        return spell.cast()
