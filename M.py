
N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = [[0 for j in range(K+1)] for i in range(N+1)]
dp[0][0] = 1
cum = [0 for j in range(K+1+1)]
mod = 10**9 + 7
for i in range(N):
    cum[0] = 0
    for j in range(K+1):
        cum[j+1] = (cum[j] + dp[i][j]) % mod
    for j in range(K+1):
        dp[i+1][j] = (cum[j+1] - cum[max(0, j-A[i])]) % mod

print(dp[N][K])