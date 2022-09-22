# 에라토스테네스의 채

SIZE = 2 ** 12
sieve = [False,False] + [True * SIZE]
arr = list()
def check(n):
    for i in range(2,n):
        if sieve[i]:
            arr.append(i)
            for j in range(2*i,SIZE,i):
                sieve[j] = False

# 비트마스킹을 활용한 에라토스 테네스의 채

SIZE = 2 ** 12
sieve = [255 for _ in range(SIZE//8+1)]
def set_composite(n):
    sieve[n>>3] &= ~(1 << (n & 7))
set_composite(0)
set_composite(1)
def is_prime(n):
    return True if sieve[n>>3] & (1 << (n & 7)) else False
for i in range(2,int(SIZE**(1/2))):
    if is_prime(i):
        for j in range(i * i, SIZE+1, i):
            set_composite(j)




# 개미 수열

n = int(input())
arr = [1]
arr1 = []
for _ in range(n-1):
    t = arr[0]
    cnt = 0
    for i in arr:
        if t == i:
            cnt += 1
        else:
            arr1.append(t);arr1.append(cnt)
            t = i; cnt = 1
    arr1.append(t);arr1.append(cnt)
    arr = arr1
    arr1 = []
print(sum(arr))


# 총알의 속도

a,b = map(float,input().split())
n = (a+b) / (1+((a+b)/(299792458**2)))


# 분할 정복을 이용한 거듭제곱

def fpow(N,n,m):
    if n == 1:
        return N % m
    else:
        x = fpow(N,n//2,m)
        if n % 2 == 0:
            return (x * x) % m
        else:
            return (x * x * N) % m


# 밀러 라빈

from random import randint

def primalityTest(n, k):
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d >>= 1
    for i in range(k):
        rand = randint(2, n - 2)
        x = rand**d % n         # offending line
        if x == 1 or x == n - 1:
            continue
        for r in range(s):
            toReturn = True
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                toReturn = False
                break
        if toReturn:
            return False
    return True

print(primalityTest(2700643,1))


# 소인수 구하기

def f(x):
    arr = list()
    i = 2
    while i <= x:
        if x % i == 0:
            arr.append(i)
            x = x / i
        else:
            i = i + 1
    return arr

# 유클리드 호제법

def gcd(a, b):
    if a == b:
        return a
    if a < b:
        a,b=b,a
    for _ in range(b):
        if b == 0:
            return a
        c = a % b
        a = b
        b = c

# 이항계수

def fac(n):
    res = 1
    for i in range(2,n+1):
        res *= i
    return res
n,r = map(int,input().split())
print((fac(n)//fac(r)//fac(n-r)))


# 가장 큰 증가하는 부분 수열 ( LIS )
# 11053번

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i], dp[j]+1)
print(max(dp))


# 에라토스 테네스의 체

def prime(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           
            for j in range(i+i, n, i): 
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]



# KMP

def fail(s):
    n = len(s); arr = []
    for i in range(1,n+1):
        j = 0
        while(j and s[i] != s[j]): j = arr[j - 1]
        if( s[i] == s[j]): arr[i] = ++j
    return arr

def KMP(a,b):
    n = len(a); m = len(b)
    ret,f = fail(b)

    for i in range(1,n+1):
        while (j and a[i] != b[j]): j = f[j-1]
        if a[i] == b[j] and ++j == m:
            ret.append(i-m+1)
            j = f[j-1]
    return ret

# 요세푸스 문제

import sys;sys.setrecursionlimit(10000)
def f(n,k):
    if n == 1:
        return 0
    if k == 1:
        return n - 1
    if k > n:
        return (f(n-1,k)+k)%n+1
    cnt = n//k
    res = f(n-cnt,k)
    res -= n%k
    if res < 0: res += n
    else: res += res // (k - 1)
    return res


