n = int(input())
count = 0
for i in range(n):
    current_num = int(input())
    j = 2
    while j <= current_num**(1/2):
        if current_num % j == 0:
            count +=1
            break
        j += 1

print(n-count)