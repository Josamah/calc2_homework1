""" This is our calculation base class / Abstract class"""


class Calculation:
    """this is our calculation class/ Abstract class"""
    # constructor and it is the first function called when an object of the class is instantiated
    def __init__(self, value_a, value_b):
        # self references the instantiated object of the class
        self.value_a = value_a
        self.value_b = value_b

    """Class Factory Method"""
    @classmethod
    def create(cls, value_a, value_b):
        return cls(value_a, value_b)
