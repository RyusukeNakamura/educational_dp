n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [10 ** 9] * n
dp[0] = 0

for i in range(1, n):
    j = max(0, i - k)
    hi = h[i]
    dp[i] = min(dpj + abs(hi - hj) for dpj, hj in zip(dp[j:i], h[j:i]))

print(dp[-1])