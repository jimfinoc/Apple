from __future__ import unicode_literals
from os.path import abspath, join, dirname
import random

__origional_author__ = 'Trey Hunner'



full_path = lambda filename: abspath(join(dirname(__file__), filename))

FILES = {
    'first:male': full_path('dist.male.first.txt'),
    'first:female': full_path('dist.female.first.txt'),
    'last': full_path('dist.all.last.txt'),
}


def get_name(filename):
    selected = random.random() * 90
    with open(filename) as name_file:
        for line in name_file:
            name, _, cummulative, _ = line.split()
            if float(cummulative) > selected:
                return name
    return ""  # Return empty string if file is empty


def get_first_name(gender=None):
    if gender is None:
        gender = random.choice(('male', 'female'))
    if gender not in ('male', 'female'):
        raise ValueError("Only 'male' and 'female' are supported as gender")
    return get_name(FILES['first:%s' % gender]).capitalize()


def get_last_name():
    return get_name(FILES['last']).capitalize()


def get_full_name(gender=None):
    return "{0} {1}".format(get_first_name(gender), get_last_name())



if __name__ == "__main__":
    print(get_full_name())
    print(get_last_name())
    print(get_full_name('male'))
    print(get_full_name('female'))
    print(get_first_name('female'))
    # print full_path
