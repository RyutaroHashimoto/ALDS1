n = int(input())

prev = 10**18
res = -10**18

for i in range(n):
    r = int(input())

    if res < r - prev:
        res = r - prev
    
    if r < prev:
        prev = r

print(res)

