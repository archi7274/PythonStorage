SIZE = 2 ** 12
sieve = [False,False] + [True] * SIZE
print(len(sieve))
arr = list()
def check(n):
    for i in range(2,n):
        if sieve[i]:
            arr.append(i)
            for j in range(2*i,SIZE,i):
                sieve[j] = False

n = input()
ans = []
start = n[0]; end = n[-1]
check(int(n))
for i in range(1, len(n)):
    temp = start
    t = 0
    while temp[-1] != end[-1]:
        temp = n[t:t+i]
        t += 1
        if int(temp) in arr:
            ans.append(int(temp))
print(ans)
