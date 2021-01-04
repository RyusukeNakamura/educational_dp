import numpy as np
N = int(input())
P = list(map(float, input().split()))

dp = np.zeros((N+1, N+1))
dp[0][0] = 1
for i in range(N):
        dp[i+1][1:] += dp[i][:-1] * P[i]
        dp[i+1][:-1] += dp[i][:-1] * (1 - P[i])
print(sum(dp[N][(N+1)//2:]))