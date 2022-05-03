# https://blog.manuel1024.com/archives/143

n, k = map(int, input().split())
w = []
for i in range(n):
    w.append(int(input()))

ac = 0 
wa = 0 

# initial ac value
ac  = sum(w)

while(ac-wa > 1):
    mid = (wa+ac) // 2  # initial P is median od w

    nowk = 1
    now_w = 0
    isac = True

    for i in range(n):
        if now_w+w[i] <= mid:
             now_w += w[i]
        else:
            nowk += 1
            if w[i] <= mid:
                 now_w = w[i]
            else:
                isac = False
                break

    if nowk > k:
        isac = False

    if isac:
        ac = mid
    else:
        wa = mid

print(ac)
