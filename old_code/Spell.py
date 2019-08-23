from enum import Enum


class ActionType(Enum):
    CREATE = 1
    ABSORB = 2
    DISPLACE = 3


class Spell:
    def __init__(self, element, origin, shape, action):
        """
        Holds information on how the SpellEffects are constructed.
        :param element of type Element :
        :param origin:
        :param shape:
        :param action:
        """
        self.element = element
        self.origin = origin
        self.shape = shape
        self.action = action

    def cost(self):
        """
        calculates of this spell.
        :return:
        """
        return self.element.get_cost() * self.shape.get_cost()

    def create(self):
        print("Spell of Fire created.")
        return self

    def absorb(self):
        return

    def displace(self):
        return

    def cast(self):
        print(self.action)
        if self.action == ActionType.CREATE:
            return self.create()
        elif self.action == ActionType.ABSORB:
            self.absorb()
        else:
            self.displace()
