# 그룹 내에서 가장 잘하는 학생과 가장 못 하는 학생의 실력 차이가 D 이하여야 한다.
# E = (그룹 내의 학생들이 아는 모든 알고리즘 수 - 그룹 내의 모든 학생들이 아는 알고리즘 수) * 그룹 원 수
# 조건을 만족하는 학생들의 부분 집합 중 효율성이 최대가 되는 그룹을 뽑음
# 그룹의 효율성은?


n,m,h = map(int,input().split())
for i in range(n):
    a, b = map(int,input().split()) 
    