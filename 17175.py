a = int(input())
arr = [1, 3, 5]
if a == 0:
    print(1)
    exit()
elif a < 4:
    print(arr[a-1])
    exit()
for i in range(a-3):
    arr.append(arr[-1] + arr[-2] + 1)
print(arr[-1] % 1000000007)
