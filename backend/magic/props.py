from magic.spell import Spell


class Props:
    def __init__(self, position, velocity, health=1, mana=1):
        self.position = position
        self.velocity = velocity
        self.health = health
        self.mana = mana


class Wizard(Props):
    def __init__(self, position, velocity):
        super().__init__(position, velocity, health=100, mana=100)

    def shout(self, string):
        return Spell(string).decode_incantation(self.position).cast()
