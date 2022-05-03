a, b = map(int, input().split())
if a < b:
    temp = a
    a = b
    b = temp

gcd = b
res = 0
while gcd > 0:
    res = gcd
    gcd = a % b
    a = b
    b = gcd

print(res)
