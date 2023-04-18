temp = input()
boom = list(input())
length = len(boom)
stack = []
for i in temp:
    stack.append(i)
    if len(stack) >= length and stack[len(stack) - length:] == boom:
        for j in range(length):
            stack.pop()
if len(stack) == 0:
    print('FRULA')
else:
    for i in stack:
        print(i,end='')




