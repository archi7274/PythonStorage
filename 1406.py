from collections import deque
import sys; input = sys.stdin.readline
arr = deque(input().strip()); arr2 = deque()
for _ in range(int(input())):
    s = input().strip().split()
    if s[0] == 'L' and arr: arr2.appendleft(arr.pop())
    elif s[0] == 'D' and arr2: arr.append(arr2.popleft())
    elif s[0] == 'B' and arr: arr.pop()
    elif s[0] == 'P': arr.append(s[1])
res = arr + arr2
print(*res, sep="")
