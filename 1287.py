import sys; sys.setrecursionlimit(10**5)
arr = ['+','-','/','*']
a = input()
temp = list(a)
if temp[0] in arr:
    print('ROCK')
    exit()
for i in range(a.count('(')):
    t = temp.index('(')
    if temp[t+1] in arr:
        print('ROCK')
        exit()
for i in arr:
    for j in range(a.count(i)):
        t = temp.index(i)
        if temp[t+1] in arr:
            print('ROCK')
            exit()
if a.count('/') >= 1:
    a = a.replace('/','//')
try:
    print(int(eval(a)))
except:
    print('ROCK')