class Tile:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.objects = []
        self.state = {"Temperature": 24, "Time": 1, "Gravity": 9.81}

    def resolve_tile(self):
        for object in self.objects:
            self.state = object.interact_on(self.state)
        for object in self.objects:
            if not object.interact_from(self.state):
                self.objects.remove(object)


    def add_object(self, object):
        self.objects.append(object)

    def get_information(self):
        return str(self.coordinates) + " with world effects " + str(len(self.objects))
