class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.iterable) == 0:
            raise StopIteration
        current = self.iterable.pop()
        return current