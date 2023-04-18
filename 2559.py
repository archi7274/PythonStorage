n,k = map(int,input().split())
arr = list(map(int,input().split()))
tmp = [0]
l = 0
for i in arr:
    l += i
    tmp.append(l)
m = []
for i in range(n-k+1):
    m.append(tmp[i+k] - tmp[i])
print(max(m))

# 풀이 1

# import sys
# input = sys.stdin.readline

# n, k = map(int,input().split())
# a = list(map(int, input().split()))

# result = []
# result.append(sum(a[:k]))

# for i in range(n - k):
#     result.append(result[i] - a[i] + a[k+i])

# print(max(result))

