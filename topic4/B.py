n = int(input())
nums_n = list(map(int, input().split()))
q = int(input())
nums_q = list(map(int, input().split()))

count = 0

for search_value in nums_q:
    left_index: int = 0
    right_index: int = len(nums_n) - 1

    while left_index <= right_index:
        middle_index: int = (left_index + right_index) // 2
        middle_value: int = nums_n[int(middle_index)]

        if search_value < middle_value:
            right_index = middle_index - 1
            continue
        if search_value > middle_value:
            left_index = middle_index + 1
            continue

        count += 1
        break


print(count)
