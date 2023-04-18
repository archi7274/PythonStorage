# 오일러 피 함수
# 1. p가 소수인 경우
# 약수가 1과 자기자신 밖에 없기 때문에 모든 수와 서로소이다.
# 2. 소수 p의 거듭제곱인 경우
# 소수 p의 거듭제곱과 서로소가 아닌 경우는 p의 배수인 경우이다. 즉 p, 2p, 3p ... p^(k-1) * p => p ^ k - p ^ (k-1)
# 3. n과 m이 서로소인 경우
# n과의 서로소의 곱과 m과 서로소의 곱은 n*m과 서로소이다.

# n의 소인수를 구한 후에, 
# 각 소인수들의 (1 - 1 / p)를 구해 n에 곱해주면 서로소의 갯수를 알 수 있다.


# n = int(input())
# ans = n; num = n
# i = 2
# while i*i <= n:
#     if num % i == 0:
#         ans /= i
#         ans *= i - 1
#         while num % i == 0:
#             num /= i
#     i += 1
# if num != 1:
#     ans /= num
#     ans *= num - 1


n = int(input())
ans = n
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        while n % i == 0:
            n //= i
        ans *= (i - 1) / i
if n != 1:
    ans *= 1 - (1 / n)
print(int(ans))