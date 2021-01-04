N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = [0 for _ in range(K+1)]

for i in range(K+1):
    for a in A:
        # index=元A[j]を使ったあとの残りの石の数の状態が0ならsp[i]には1を代入
        if i - a >= 0 and dp[i - a] == 0:
            dp[i] = 1

print('First' if dp[K] else 'Second')