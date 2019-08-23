from Elements import *


class SpellEffect:
    def __init__(self, level):
        self.type = None
        self.setting_type = None
        self.base_cost = None
        self.start = None
        self.level = level

    def cost(self):
        return


class SpellEffectFire(SpellEffect):
    def __init__(self, level):
        SpellEffect.__init__(self, level)
        self.type = 'Fire'
        self.setting_type = 'Temperature'
        self.base_cost = 1

    def create(self, position, velocity, shape):
        temperature = 400 + (100 * self.level)
        return Fire(temperature, position, velocity, shape)


class SpellEffectCold(SpellEffect):
    def __init__(self, level):
        SpellEffect.__init__(self, level)
        self.type = 'Cold'
        self.setting_type = 'Temperature'
        self.base_cost = 1

    def create(self, position, velocity, shape):
        temperature = 0 - (25 * self.level)
        return Water(temperature, position, velocity, shape)

class SpellEffectEarth(SpellEffect):
    def __init__(self, level):
        SpellEffect.__init__(self, level)
        self.type = 'Earth'
        self.setting_type = 'Weight'
        self.base_cost = 1


class SpellEffectTime(SpellEffect):
    def __init__(self, level):
        SpellEffect.__init__(self, level)
        self.type = 'time'
        self.setting_type = 'Rate'
        self.base_cost = 10



