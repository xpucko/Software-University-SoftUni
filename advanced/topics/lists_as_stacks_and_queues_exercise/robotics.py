from collections import deque


def next_second(h, m, s):
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0
    return h, m, s


data = input().split(";")
robots_start_data = {}
available_robots = deque()
waiting_robots = deque()
products = deque()
time = [int(x) for x in input().split(":")]

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

for robot_info in data:
    robot_name = robot_info.split('-')[0]
    robot_time = int(robot_info.split('-')[1])
    available_robots.append([robot_name, robot_time])
    robots_start_data[robot_name] = robot_time

while products:
    for robot_inf in waiting_robots:
        name = robot_inf[0]
        robot_inf[1] -= 1
        if robot_inf[1] <= 0:
            available_robots.append([name, robots_start_data[name]])

    waiting_robots = [r for r in waiting_robots if r[1] > 0]
    time = next_second(time[0], time[1], time[2])
    current_product = products.popleft()

    if not available_robots:
        products.append(current_product)
        continue

    current_robot = available_robots.popleft()
    print(f"{current_robot[0]} - {current_product} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]")
    waiting_robots.append(current_robot)
