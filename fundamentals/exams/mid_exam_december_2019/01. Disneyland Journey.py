journey = float(input())
months = int(input())

save = 0
for month in range(1, months + 1):
    if month % 2 == 1 and month != 1:
        save -= save * 0.16
    if month % 4 == 0:
        save += save * 0.25
    save += journey * 0.25

if save < journey:
    print(f'Sorry. You need {journey - save:.2f}lv. more.')
else:
    print(f'Bravo! You can go to Disneyland and you will have {save - journey:.2f}lv. for souvenirs.')