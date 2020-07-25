from math import floor

biscuits_per_worker = int(input())
workers = int(input())
competing_factory = int(input())
monthly_biscuits = 0
for day in range(1, 31):
    daily_biscuits = workers * biscuits_per_worker
    if day % 3 == 0:
        daily_biscuits *= 0.75
    monthly_biscuits += floor(daily_biscuits)

percentage = abs(monthly_biscuits / competing_factory - 1) * 100
print(f'You have produced {monthly_biscuits} biscuits for the past month.')
print(f'You produce {percentage:.2f} percent more biscuits.') if competing_factory < monthly_biscuits \
    else print(f'You produce {percentage:.2f} percent less biscuits.')
