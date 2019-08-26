from django.db import models

DEFAULT_WORLD_SIZE = 10


class World(models.Model):
    name = models.TextField(default="")
    size = models.IntegerField(default=DEFAULT_WORLD_SIZE)
