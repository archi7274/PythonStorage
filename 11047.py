a,b = map(int,input().split())
arr = []
cnt = 0
for i in range(a):
    arr.append(int(input()))
arr.sort(reverse=True)
for i in arr:
    if b >= i:
        cnt += b // i
        b %= i
print(cnt)

