from container import Container


class Queue(Container):
    """ Subclass of Container, First in First out (FIFO)"""

    def peek(self):
        """ Returns the first element of the list without deleting it"""
        assert not self.is_empty()
        return self._items[0]

    def pop(self):
        """ Pops off the first element"""
        assert not self.is_empty()
        return self._items.pop(0)