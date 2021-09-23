import numbers
import numpy as np


class Function:
    """ Executes the method of a given function """

    def __init__(self, func):
        self.func = func

    def execute(self, element, debug=True):
        """ Executes the method of the function with the element"""
        if not isinstance(element, numbers.Number):
            raise TypeError("The element must be a number")
        result = self.func(element)

        if debug is True:
            print("Function: " + self.func.__name__
                  + "({:f}) = {:f}".format(element, result))

        return result