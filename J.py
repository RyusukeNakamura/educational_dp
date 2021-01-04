# PyPy3だとAC．
N = int(input())
A = list(map(int, input().split()))
one, two, three = 0, 0, 0
for a in A:
    if a == 1:
        one += 1
    elif a == 2:
        two += 1
    else:
        three += 1

dp = [[[0 for k in range(N+1)] for j in range(N+1)] for i in range(N+1)]

for k in range(three+1):
    for j in range(two+three+1-k):
        for i in range(N+1-k-j):
            if i==0 and j==0 and k==0:
                continue

            res = 0.0
            if i > 0:
                res += dp[i-1][j][k] * i
            if j > 0:
                res += dp[i+1][j-1][k] * j
            if k > 0:
                res += dp[i][j+1][k-1] * k
            res += N
            res /= (i + j + k)
            dp[i][j][k] = res

print(dp[one][two][three])