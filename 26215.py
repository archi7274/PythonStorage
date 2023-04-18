
# 5 5 5 - 9
# 2 2 - 2


a = int(input())
arr = list(map(int,input().split()))
cnt = 0
n = 0
while True:
    arr.sort()
    if len(arr) > 1:
        cnt += 1
        arr[-1] -= 1
        arr[-2] -= 1
    elif len(arr) == 1:
        cnt += arr.pop()
        break
    else:
        break
    for _ in range(arr.count(0)):
        arr.remove(0)
if cnt > 1440:
    print(-1)
else:
    print(cnt)