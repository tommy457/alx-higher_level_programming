#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """Define MyList"""

    def print_sorted(self):
        """Print a list in sorted ascending order
        Args:
            self (list): list of ints
        """
        print(sorted(self))
