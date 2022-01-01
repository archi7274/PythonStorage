# 알파벳을 정렬하라

# arr = ['b', 'c', 'a', 'f', 't', 'e']
# print(arr)
# # 정렬
# arr.sort()
# print(arr)
# print(len(arr))

# 문제 : 아래 알파벳 중 가장 빨리 나오는 것과 가장 늦게 나오는 알파벳을 출력하시오.
# arr['t','b','c','k','u','n']
# arr = ['t', 'b', 'c', 'k', 'u', 'n']
# arr.sort()
# print(arr)
# print(arr[0],arr[len(arr)-1])


# [문제]
# score = [55,78,99,34,87]
# 1위 점수를 출력하시오.

score = [55, 78, 99, 34, 87]
print('1위 점수는 ')
# score.sort(reverse=True)
# print(score[0])
print(max(score))
print(min(score))