def LCS(s1, s2):
    r, h = len(s1), len(s2)
    dp = [[0] * (h + 1) for _ in range(r + 1)]
    for i in range(1, r + 1):
        for j in range(1, h + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    result = []
    cur = dp[-1][-1]
    while len(result) != dp[-1][-1]:
        if dp[r - 1][h] == cur:
            cur = dp[r - 1][h]
            r -= 1
        elif dp[r][h - 1] == cur:
            cur = dp[r][h - 1]
            h -= 1
        else:
            result.append(s1[r - 1])
            cur = dp[r - 1][h - 1]
            r -= 1
            h -= 1
    return ''.join(result[::-1])

s1 = input()
s2 = input()
s3 = input()
