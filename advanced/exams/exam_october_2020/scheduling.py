jobs, index = [int(x) for x in input().split(', ')], int(input())
print(sum([jobs[i] for i in range(len(jobs)) if jobs[i] <= jobs[index]]))
