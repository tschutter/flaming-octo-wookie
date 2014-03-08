#!/usr/bin/env python2

import random
import sys

# Create a dict (dictionary) of races.  The value of each race is a
# dict of sexes.  The value of each sex is a tuple of minimum height
# and a variant in height.
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
    """Return a random height based upon race and sex."""
    height_data = HEIGHT_DATA[race][sex]           # Could combine with next line.
    height_min, height_variant = height_data       # Unpack tuple.
    height = height_min + random.randint(0, height_variant)
    return height

def main():
    print("Let's generate some characters!")
    for race in ["human", "dwarf", "halfling"]:    # Loop through races.
        for sex in ["male", "female", "sexless"]:  # Loop through sexes.
            for i in range(3):                     # Let's do multiple examples.
                height = get_height(race, sex)     # Calculate height.
                print(                             # Output.
                    "%s %s #%i height = %i" %
                    (race, sex, i, height)
                )

if __name__ == "__main__":
    sys.exit(main())
