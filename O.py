N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
mod = 10**9 + 7
dp = [0 for j in range(1 << N)]
dp[0] = 1

for S in range(1 << N):
    for j in range(N):
        # Sのj bit目が1か．
        if (S >> j) & 1 and A[bin(S).count("1")-1][j]:
            # j番目を固定したときの場合の数．集合Sから要素jを除外．
            dp[S] += dp[S ^ (1 << j)]
            dp[S] %= mod
print(dp[(1 << N) - 1])