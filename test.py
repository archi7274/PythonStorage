for i in range(int(input())):
    a = list(map(int,input().split()))[1:]
    s = sum(a) / len(a)
    cnt = 0
    for j in a:
        if j > s:
            cnt += 1
    t = cnt / len(a) * 100
    print("%.3f"%t+"%")