class Elements:
    def __init__(self, position, velocity, shape):
        self.position = position
        self.velocity = velocity
        self.shape = shape

    def interact_on(self, state):
        return state

    def interact_from(self, state):
        pass


class Fire(Elements):
    def __init__(self, temperature, position, velocity, shape):
        Elements.__init__(self, position, velocity, shape)
        self.temperature = temperature

    def interact_on(self, state):
        state["Temperature"] = (state["Temperature"] + self.temperature) / 2
        return state

    def interact_from(self, state):
        self.temperature = state["Temperature"]
        return self.check_status()

    def check_status(self):
        if self.temperature < 300:
            return False
        else:
            return True


class Water(Elements):
    def __init__(self, temperature, position, velocity, shape):
        Elements.__init__(self, position, velocity, shape)
        self.temperature = temperature

    def interact_on(self, state):
        state["Temperature"] = (state["Temperature"] + self.temperature) / 2
        return state

    def interact_from(self, state):
        self.temperature = state["Temperature"]
        return True

    def check_status(self):
        if self.temperature < 0:
            return True
        elif self.temperature > 100:
            return True
        else:
            return True
