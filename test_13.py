num = int(input('자연수 입력:'))
fac = 1

for i in range(1, num + 1, 1):
    fac *= i
print(f'{num}팩토리얼은 {fac}입니다')