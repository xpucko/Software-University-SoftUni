from collections import deque


def solve(customers, taxis):
    total_time = 0
    while customers:
        if not taxis:
            return f'Not all customers were driven to their destinations\nCustomers left: {", ".join(map(str, customers))}'
        customer = customers.popleft()
        taxi = taxis.pop()
        if customer <= taxi:
            total_time += customer
        else:
            customers.appendleft(customer)

    if not customers:
        return f'All customers were driven to their destinations\nTotal time: {total_time} minutes'


my_customers = deque([int(x) for x in input().split(', ')])
my_taxis = [int(x) for x in input().split(', ')]
print(solve(my_customers, my_taxis))