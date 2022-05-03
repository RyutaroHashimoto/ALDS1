n = int(input())
nums_n = list(map(int, input().split()))
q = int(input())
nums_q = list(map(int, input().split()))

count = 0
for i in set(nums_n):
    for j in nums_q:
        if i == j:
            count += 1
            break

print(count)