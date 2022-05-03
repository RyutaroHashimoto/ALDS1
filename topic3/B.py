from collections import Counter, deque

n, q = map(int, input().split())
queue = deque([])

for i in range(n):
    name, time = input().split()
    time = int(time)
    queue.append([name, time])

totaltime = 0

while queue:
    [name, time] = queue.popleft()
    if time <= q:  
        totaltime += time
        print(name, totaltime)
    else:
        time -= q
        queue.append([name, time])  
        totaltime += q

