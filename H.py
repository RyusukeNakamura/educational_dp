H, W = map(int, input().split())
A = [list(input()) for j in range(H)]

mod = 10**9 + 7
dp = [[0 for j in range(W+1)] for i in range(H+1)]
dp[1][1] = 1

for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            continue

        dp[i+1][j+1] += dp[i][j+1] % mod
        dp[i+1][j+1] += dp[i+1][j] % mod

print(dp[-1][-1]%mod)