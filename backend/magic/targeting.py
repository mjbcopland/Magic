class Target:
    def __init__(self, position, base_cost=None, level=None):
        self.position = position
        self.base_cost = base_cost
        self.level = level

    @property
    def cost(self):
        return self.base_cost * self.level

    @property
    def properties(self):
        return dict(position=self.position, velocity=self.velocity)

    @property
    def velocity(self):
        return None


class Self(Target):
    def __init__(self, position, base_cost=None, level=1):
        super().__init__(position, base_cost, level)

    @property
    def velocity(self):
        return 0


class Point(Target):
    def __init__(self, position, level):
        super().__init__(position, 1, level)

    @property
    def velocity(self):
        return self.level * 5
