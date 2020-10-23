customers = [int(x) for x in input().split(', ')]
taxis = [int(x) for x in input().split(', ')]
total_time = 0

while customers and taxis:
    customer = customers[0]
    taxi = taxis[-1]
    if customer <= taxi:
        taxis.pop()
        total_time += customers.pop(0)
    else:
        taxis.pop()

if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print(f'Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(map(str, customers))}')
