#!/usr/bin/python3
"""This is the square module"""


class square():
    """This is the square class"""

    side = 0

    def __init__(self, *args, **kwargs):
        """This is the initializer"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.side * self.side

    def PermiterOfMySquare(self):
        """The perimeter of the square"""
        return (self.side * 4)

    def __str__(self):
        """The string representation of the the squre"""
        return "{}/{}".format(self.side, self.side)


if __name__ == "__main__":

    s = square(side=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
