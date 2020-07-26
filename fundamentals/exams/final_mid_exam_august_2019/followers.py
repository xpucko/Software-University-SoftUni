followers = {}
while True:
    line = input().split(': ')
    if line[0] == 'Log out':
        print(f'{len(followers)} followers')
        for k, v in sorted(followers.items(), key=lambda x: (-x[1][0], x[0])):
            print(f'{k}: {sum(v)}')
        break
    name = line[1]
    if line[0] == 'New follower':
        if name not in followers:
            followers[name] = [0, 0]
    elif line[0] == 'Like':
        if name not in followers:
            followers[name] = [0, 0]
        followers[name][0] += int(line[2])
    elif line[0] == 'Comment':
        if name not in followers:
            followers[name] = [0, 0]
        followers[name][1] += 1
    elif line[0] == 'Blocked':
        if name in followers:
            del followers[name]
        else:
            print(f"{name} doesn't exist.")