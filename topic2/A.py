n = int(input())
nums = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(n-1, i, -1):
        if nums[j] < nums[j-1]:
            temp = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = temp
            count += 1

print(*nums)
print(count)