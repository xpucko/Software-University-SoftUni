print([n for sublist in [[int(x) for x in input().split(', ')] for _ in range(int(input()))] for n in sublist])