def get_repeating_DNA(string):
    d = {}
    result = []
    for i in range(len(string)):
        substring = string[i:i + 10]
        d[substring] = d.get(substring, 0) + 1
    [result.append(key) for key, value in d.items() if value > 1]
    return result