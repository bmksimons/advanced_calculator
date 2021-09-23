import numbers


class Operator:
    """ Executes the method of a given operator """

    def __init__(self, operator, strength):
        self.operator = operator
        self.strength = strength

    def execute(self, element, element2, debug=True):
        """ Executes the method of the operator with the two given elements """
        if not isinstance(element, numbers.Number):
            raise TypeError("The element must be a number")
        result = self.operator(element, element2)
        if debug is True:
            print("Function: " + self.operator.__name__
                  + "({:f}) = {:f}".format(element, result))

        return result

    def get_strength(self):
        return self.strength

    def __str__(self):
        self.operator.__str__()