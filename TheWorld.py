import Location from Location


class TheWorld:
    def __init__(self):
        self.locations = None
        self.prepareLocations()

    def prepareLocations(self):
        self.locations = [Location(x,y) for x,y in range(10)]
        print(self.locations)
