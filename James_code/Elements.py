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
            return None
        else:
            return self


class Water(Elements):
    def __init__(self, temperature, position, velocity, shape):
        Elements.__init__(self, position, velocity, shape)
        self.temperature = temperature

    def interact_on(self, state):
        if (state["Temperature"] + self.temperature)/2 < state["Temperature"]:
            state["Temperature"] = (state["Temperature"] + (self.temperature*4.5)/2)
        else:
            state["Temperature"] = (state["Temperature"] + self.temperature)/2

        if state["Temperature"] < -273:
            state["Temperature"] = -273
        return state

    def interact_from(self, state):
        self.temperature = state["Temperature"]
        return self.check_status()

    def check_status(self):
        if self.temperature < 0:
            return Ice(self.temperature, self.position, self.velocity, self.shape)
        elif self.temperature > 100:
            return Steam(self.temperature, self.position, self.velocity, self.shape)
        else:
            return self


class Ice(Water):
    def __init__(self, temperature, position, velocity, shape):
        Water.__init__(self, temperature, position, velocity, shape)

    def check_status(self):
        if self.temperature < 0:
            return self
        elif self.temperature > 100:
            return Steam(self.temperature, self.position, self.velocity, self.shape)
        else:
            return Water(self.temperature, self.position, self.velocity, self.shape)


class Steam(Water):
    def __init__(self, temperature, position, velocity, shape):
        Water.__init__(self, temperature, position, velocity, shape)

    def check_status(self):
        if self.temperature < 0:
            return Ice(self.temperature, self.position, self.velocity, self.shape)
        elif self.temperature > 100:
            return self
        else:
            return Water(self.temperature, self.position, self.velocity, self.shape)