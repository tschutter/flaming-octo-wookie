#!/usr/bin/env python2

import random
import sys

HEIGHT_DATA = {
    "human": {
        "male": (50, 8),
        "female": (40, 6),
        "sexless": (0, 0)
    },
    "dwarf": {
        "male": (30, 6),
        "female": (25, 4),
        "sexless": (0, 0)
    },
    "halfling": {
        "male": (45, 12),
        "female": (35, 8),
        "sexless": (30, 8)
    },
}

def get_height(race, sex):
    height_data = HEIGHT_DATA[race][sex]
    height_min, height_variant = height_data
    height = height_min + random.randint(0, height_variant)
    return height

def main():
    for race in ["human", "dwarf", "halfling"]:
        for sex in ["male", "female", "sexless"]:
            for i in range(3):
                print(
                    "%s %s #%i height = %i" %
                    (race, sex, i, get_height(race, sex))
                )

if __name__ == "__main__":
    sys.exit(main())
