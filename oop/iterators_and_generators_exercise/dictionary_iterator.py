class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.dictionary):
            key = self.keys[self.current]
            value = self.dictionary[key]
            self.current += 1
            return key, value
        raise StopIteration