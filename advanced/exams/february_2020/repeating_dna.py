def get_repeating_dna(string):
    d = {}
    result = []
    for i in range(len(string)):
        substring = string[i:i + 10]
        d[substring] = d.get(substring, 0) + 1
    for key, value in d.items():
        if value > 1:
            result.append(key)
    return result