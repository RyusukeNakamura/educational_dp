import numpy as np

s = np.array(list(input()))
t = np.array(list(input()))
equal = (s[:, None] == t[None, :]) # 対応表の作成

slen, tlen = len(s), len(t)
dp = [[0 for j in range(tlen+1)] for i in range(slen+1)]

# dp[i][j]...sをi-1文字目, tをj-1文字目まで見たときの最長共通部分の長さ
for i in range(slen):
    dp[i+1][1:] = np.maximum(dp[i][:-1] + equal[i], dp[i][1:]) # 共通文字発見時，加えた方が大きくなるかどうか
    dp[i+1] = np.maximum.accumulate(dp[i+1]) # 累積最大値


l = dp[slen][tlen]
ans = ['' for _ in range(l)]
i, j = slen - 1, tlen - 1
for _ in range(10**9):
    if l == 0:
        break

    if s[i] == t[j]:
        ans[l-1] = s[i]
        i -= 1
        j -= 1
        l -= 1
    elif dp[i+1][j+1] == dp[i][j+1]:
        i -= 1
    else:
        j -= 1

print(''.join(ans))