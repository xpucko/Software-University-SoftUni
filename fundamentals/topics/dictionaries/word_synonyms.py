n = int(input())
dictionary = {}

for _ in range(n):
    word, synonym = input(), input()
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonym)

for key, value in dictionary.items():
    print(f"{key} - {', '.join(value)}")
