class SpellEffect:
    def __init__(self):
        self.element = None
        self.power = None

    def interact(self, other_spell_effect):
        # self.element and other_spell_effect.element if self.power is higher.
        return