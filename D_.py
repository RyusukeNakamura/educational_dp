import numpy as np

n, w = map(int, input().split())
wv_list = [[int(i) for i in input().split()] for i in range(n)]

dp = np.zeros(w+1)

for wv in wv_list:
    w = wv[0]
    v = wv[1]
    # 2つのarrayをインデックスごとに比較して大きい方を返す．
    dp[w:] = np.maximum(dp[:-w]+v, dp[w:])

print(int(np.max(dp)))
