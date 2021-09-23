class Container:
    """ Superclass for queue and stack classes """

    def __init__(self):
        self._items = []

    def size(self):
        """ Returns the length of the list self._items """
        return len(self._items)

    def is_empty(self):
        """ Returns True if self._items is empty, False otherwise """
        return len(self._items) == 0

    def get_items(self):
        """ Returns the container as a list """
        return self._items

    def push(self, item):
        """ Adds item to end of self._items """
        self._items.append(item)

    def pop(self):
        """ Pops of and returns the correct element in self._items depending on the container """
        raise NotImplementedError

    def peek(self):
        """ Returns the top element without removing it"""
        raise NotImplementedError