n = int(input())
nums = list(input().split())
nums_ = nums[:]

for i in range(n):
    for j in range(n-1, i, -1):
        if nums[j][1] < nums[j-1][1]:
            temp = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = temp

print(*nums)
print('Stable')

for i in range(n):
    min = i
    for j in range(i, n):
        if nums_[j][1] < nums_[min][1]:
            min = j
    if min == i:
        continue
    temp = nums_[i]
    nums_[i] = nums_[min]
    nums_[min] = temp

print(*nums_)
if nums == nums_:
    print('Stable')
else:
    print('Not stable')
