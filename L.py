import numpy as np
N = int(input())
A = list(map(int, input().split()))
dp = np.zeros((N+1, N+1), dtype='int64')
# dp[m][i]: 区間[i,M+i]のときのX-Y
for m in range(N):
    if (N - m) % 2 != 0:
        dp[m+1][:N-m] = np.maximum(dp[m][1:N-m+1] + A[:N-m], dp[m][:N-m] + A[m:])
    else:
        dp[m+1][:N-m] = np.minimum(dp[m][1:N-m+1] - A[:N-m], dp[m][:N-m] - A[m:])

print(dp[N][0])