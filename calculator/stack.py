from container import Container


class Stack(Container):
    """ Subclass of Container, Last in First out (LIFO)"""

    def peek(self):
        """ Returns the first element of the list without deleting it"""
        assert not self.is_empty()
        return self._items[-1]

    def pop(self):
        """ Pops off the first element"""
        assert not self.is_empty()
        return self._items.pop()