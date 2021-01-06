N = int(input())
A = list(map(int, input().split()))
dp = [[0 for j in range(N+1)] for i in range(N+1)]
flg = [[0 for j in range(N+1)] for i in range(N+1)]
cum =[0]
for a in A:
    cum.append(cum[-1] + a)

def rec(i, j):
    if flg[i][j]:
        return dp[i][j]
    flg[i][j] = 1
    if i == j:
        return 0
    
    tmp = 10**15
    for k in range(i, j):
        tmp = min(tmp, rec(i, k) + rec(k+1, j))
    dp[i][j] = tmp + (cum[j] - cum[i-1])
    return dp[i][j]

print(rec(1, N))