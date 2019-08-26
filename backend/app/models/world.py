from django.db import models

DEFAULT_WORLD_SIZE = 10


class World(models.Model):
    size = models.IntegerField(default=DEFAULT_WORLD_SIZE)
