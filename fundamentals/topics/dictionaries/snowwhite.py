dwarfs = {}
colors = {}

while True:
    data = input().split(" <:> ")
    if data[0] == "Once upon a time":
        for key, value in sorted(dwarfs.items(), key=lambda x: (-x[1][0], -colors[x[1][1]])):
            name, [physic, color] = key[1], value
            print(f"({color}) {name} <-> {physic}")
        break

    dwarf_name, color, physics = data[0], data[1], int(data[2])
    if (color, dwarf_name) in dwarfs:
        if physics > dwarfs[color, dwarf_name][0]:
            dwarfs[color, dwarf_name] = [physics, color]
    else:
        colors[color] = colors.get(color, 0) + 1
        dwarfs[color, dwarf_name] = [physics, color]