s = list(input())
cnt = 0
square = 0
for i in range(len(s)):
    if square == 1:
        if s[i] == s[i].upper():
            cnt += 1
        else:
            cnt += 1
            if i != len(s) - 1:
                if s[i+1] == s[i+1].lower():
                    square = 0
                    cnt += 1
                else:
                    cnt += 1
            else:
                cnt += 1
    else:
        if s[i] == s[i].lower():
            cnt += 1
        else:
            cnt += 1
            if i != len(s) - 1:
                if s[i+1] == s[i+1].upper():
                    square = 1
                    cnt += 1
                else:
                    cnt += 1
            else:
                cnt += 1
print(cnt)
                
                