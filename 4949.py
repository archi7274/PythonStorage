temp = ''
t = []
while True:
    temp = input()
    if temp == '.':
        break
    st = list(temp)

    a = False

    stack = list()
    if st[-1] != '.':
        t.append('no')
        continue
    for i in st:
        print(stack)
        if i == '[' or i == '(':
            stack.append(i)
        if i == ']':
            if len(stack) == 0 or stack.pop() != '[':
                t.append('no')
                a = True
                break
        elif i == ')':
            if len(stack) == 0 or stack.pop() != '(':
                t.append('no')
                a = True
                break
    if a == True:
        continue
    if stack:
        t.append('no')
    else:
        t.append('yes')
for i in t:
    print(i)
