class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= (self.count * self.step) - self.step:
            result = self.current
            self.current += self.step
            return result
        raise StopIteration