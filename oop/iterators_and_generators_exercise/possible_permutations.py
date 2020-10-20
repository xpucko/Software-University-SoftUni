import itertools


def possible_permutations(seq):
    for x in itertools.permutations(seq):
        yield list(x)