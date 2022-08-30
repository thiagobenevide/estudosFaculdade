class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queque:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def size(self):
        return self._size

    