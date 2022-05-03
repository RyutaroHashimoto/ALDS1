n = int(input())
A = list(map(int, input().split()))

for i in range(n):
    key = A[i]
    j = i -1
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = key
    print(*A)

