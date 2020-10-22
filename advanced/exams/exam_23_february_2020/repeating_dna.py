import collections


def get_repeating_dna(string):
    total_dna = collections.Counter(string[i:i + 10] for i in range(len(string)))
    return [key for key in total_dna if total_dna[key] > 1]
