n = int(input())
nums = list(map(int, input().split()))
count = 0
for i in range(n):
    min = i
    for j in range(i, n):
        if nums[j] < nums[min]:
            min = j
    if min ==i:
        continue
    temp = nums[i]
    nums[i] = nums[min]
    nums[min] = temp
    count += 1
    

print(*nums)
print(count)
