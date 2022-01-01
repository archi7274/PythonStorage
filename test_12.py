import random

arr=list() # arr을 리스트로 선언
# arr=[] #위와 같음
# print(arr) #빈 리스트

#로또 번호 생성기
for i in range(6):
    arr.append(random.randint(1,46))

print(arr)

#arr에서 가장 큰 수를 출력하시오
print(max(arr))

#리스트에서 두 번쨰 큰 값을 출력하시오.
arr.sort()
print(arr[len(arr)-2])



#
# from random import randint
#
# a1 = "오늘도 행복하세요"
# a2 = "폭염 주의하세요"
# a3 = "오늘 로또를 사세요"
# a4 = "당신은 천재에요"
# a5 = "영화 무료 쿠폰을 보내드립니다"
#
# print(":::오늘의 운세:::")
# c = randint(1, 5)
# if c == 1:
#     d = a1
# elif c == 2:
#     d = a2
# elif c == 3:
#     d = a3
# elif c == 4:
#     d = a4
# elif c == 5:
#     d = a5
#
# print(d)
