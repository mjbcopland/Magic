from magic.effects import EffectType, FireEffect, ColdEffect, LightningEffect
from magic.shapes import Square, Rectangle
from magic.targeting import Point
from util.enums import make_enum


SpellAction = make_enum("SpellAction", ("Create", "Absorb", "Displace"))


class Spell:
    def __init__(self, incantation):
        self.incantation = incantation
        self.element = None
        self.action = None
        self.shape = None
        self.target = None
        self.affix = None

    def decode_incantation(self, position):
        # TODO: put into another class to map the X -> SpellEffectX Can have a list of (enum, lambda)
        components = self.incantation.split()
        if components[0] == EffectType.FIRE.value:
            self.element = FireEffect(int(components[1]))
            self.action = SpellAction(components[2])
        elif components[0] == EffectType.COLD.value:
            self.element = ColdEffect(int(components[1]))
            self.action = SpellAction(components[2])
        elif components[0] == EffectType.LIGHTNING.value:
            self.element = LightningEffect(int(components[1]))
            self.action = SpellAction(components[2])
        if components[3] == "Square":
            self.shape = Square()
        elif components[3] == "Rectangle":
            self.shape = Rectangle()
        if components[4] == "Point":
            self.target = Point(position, int(components[5]))

        return self

    def cast(self):
        if self.action == SpellAction.CREATE:
            return self.element.create(self.shape, **self.target.properties)
        # TODO absorb and displace
        # elif self.action == SpellAction.ABSORB:
        #     self.element.absorb()
        # elif self.action == SpellAction.DISPLACE:
        #     self.element.displace()

        raise SpellError(f"Cannot cast action '{self.action}'")

    def cost(self):
        return


class SpellError(Exception):
    pass
