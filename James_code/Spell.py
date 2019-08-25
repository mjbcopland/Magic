class Spell:
    def __init__(self, effect, shape, target):
        self.spell_effect = effect  # Tile-wide effect
        _, self.spell_effect.velocity = target.properties()
        self.shape = shape
        self.target = target
        self.affix = None

    def cost(self):
        return
