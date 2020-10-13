class vowels:
    def __init__(self, string):
        self.string = string
        self.index = 0
        self.searched = 'aoueiyAOUEIY'

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.string):
            raise StopIteration
        current_index = self.index
        self.index += 1
        if self.string[current_index] in self.searched:
            return self.string[current_index]
        else:
            return self.__next__()