
class Elements:
    def __init__(self, position, velocity, shape):
        self.position = position
        self.velocity = velocity
        self.shape = shape


class Fire(Elements):
    def __init__(self, temperature, position, velocity, shape):
        Elements.__init__(self, position, velocity, shape)
        self.temperature = temperature


class Water(Elements):
    def __init__(self, temperature, position, velocity, shape):
        Elements.__init__(self, position, velocity, shape)
        self.temperature = temperature

    def check_status(self):
        if self.temperature < 0:
            return print('Ice')
        elif self.temperature > 100:
            return print('Steam')
        else:
            return print('Water')