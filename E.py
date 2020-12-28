import numpy as np

N, W = map(int, input().split())
wv_list = [[int(i) for i in input().split()] for i in range(N)]

dp = np.ones(10**5 + 1, dtype='int64') * (10**9 + 1)
dp[0] = 0

for w, v in wv_list:
    # 同じ価値で重さが最小値の方の要素を返す
    dp[v:] = np.minimum(dp[:-v]+w, dp[v:])

ans = 0
for v, w in enumerate(dp):
    if w <= W:
        ans = v

print(ans)
print(dp)