n, w = map(int, input().split())
shina = tuple(tuple(map(int, input().split())) for _ in range(n))

dp = [[0 for i in range(w+1)] for j in range(n+1)]

for i, wv in enumerate(shina):
    wi = wv[0]
    vi = wv[1]
    dpi = dp[i]

    for sum_w in range(w+1):
        # 荷物iを選択する（ただし最大重みを超えない）とき
        if sum_w - wi >= 0:
            dp[i+1][sum_w] = max(dp[i+1][sum_w], dpi[sum_w - wi] + vi)
        
        # 荷物iを選択しないとき
        dp[i+1][sum_w] = max(dp[i+1][sum_w], dpi[sum_w])

print(dp[-1][-1])