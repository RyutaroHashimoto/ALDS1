# Reference: https: // mtdtx9.hatenablog.com/entry/2017/04/24/230941

stack = []
res = []

input = input()

for i, v in enumerate(input):
    if v == '\\':
        stack.append(i)
    elif v == '/' and len(stack) > 0:
        j = stack.pop()
        if len(res) == 0:
            res.append((j, i - j))
        else:
            last_lake = res.pop()
            if j > last_lake[0]:
                res.append(last_lake)
                res.append((j, i - j))
            else:
                temp = i - j
                if len(res) ==0:
                    res.append((j, temp+last_lake[1]))
                    continue
                while(last_lake[0] >= j):
                    temp += last_lake[1]
                    if len(res)==0:
                        break
                    last_lake = res.pop()
                else:
                   res.append(last_lake)
                res.append((j, temp))

result = []
for i in res:
    result.append(i[1])
print(sum(result))
if len(res)==0:
    print(0)
else:
    print(len(res), end=' ')
    print(*result)
