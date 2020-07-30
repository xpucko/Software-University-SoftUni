bands = {}
time_played = {}
while True:
    data = input().split('; ')
    if data[0] == 'start of concert':
        print(f'Total time: {sum(time_played.values())}')
        [print(f'{band} -> {time}') for band, time in sorted(time_played.items(), key=lambda x: (-x[1], x[0]))]
        final_band = input()
        print(final_band)
        [print(f'=> {bands[final_band][i]}') for i in range(len(bands[final_band]))]
        break

    band_name = data[1]
    if data[0] == 'Add':
        members = data[2]
        if band_name not in bands:
            bands[band_name] = []
        [bands[band_name].append(member) for member in members.split(', ') if member not in bands[band_name]]
    elif data[0] == 'Play':
        time = int(data[2])
        if band_name not in time_played:
            time_played[band_name] = time
        else:
            time_played[band_name] += time