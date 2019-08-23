from James_code.TheWorld import WorldEffect


class SpellEffect(WorldEffect):
    def __init__(self):
        """
        The mediator class which interfaces with the World.
        """
        self.element = None
        self.power = None

    def interact(self, other_spell_effect):
        # self.element and other_spell_effect.element if self.power is higher.
        return

