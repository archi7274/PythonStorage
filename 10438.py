n = int(input())
for j in range(2, n + 1):
    ans = j; cnt = j
    for i in range(2, int(j**0.5)+1):
        if j % i == 0:
            while j % i == 0:
                j //= i
        ans *= (i - 1) / i
    if n != 1:
        ans *= 1 - (1 / n)
    if int(ans) * j == n:
        print(j)
        exit()
print(-1)