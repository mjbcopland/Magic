from enum import Enum
from collections import OrderedDict
from inflection import underscore


def make_enum(name, options):
    return Enum(
        name, OrderedDict(((underscore(option).upper(), option) for option in options))
    )
