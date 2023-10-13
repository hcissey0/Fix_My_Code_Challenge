#!/usr/bin/python3
"""
User class
"""


class User():
    """ Documentation not long enough"""

    def __init__(self):
        """ Documentation not long enough"""
        self.__email = None

    @property
    def email(self):
        """ Documentation not long enough"""
        return self.__email

    @email.setter
    def email(self, value):
        """ Documentation not long enough"""
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
