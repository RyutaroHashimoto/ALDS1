input = list(input().split())
stack = []

for i in input:
    if i == '*':
        m = stack.pop()
        n = stack.pop()
        stack.append(m*n)
    elif i == '+':
        m = stack.pop()
        n = stack.pop()
        stack.append(m+n)
    elif i == '-':
        m = stack.pop()
        n = stack.pop()
        stack.append(n-m)
    else:
        stack.append(int(i))

print(*stack)