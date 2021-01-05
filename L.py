import sys
sys.setrecursionlimit(10**8)
N = int(input())
A = list(map(int, input().split()))

dp = [[0 for j in range(N)] for i in range(N)]
flg = [[False for j in range(N)] for i in range(N)]

def rec(i:int, j:int):
    if flg[i][j]:
        return dp[i][j]
    if i==j:
        dp[i][j] = A[i]
        return dp[i][j]
    flg[i][j] = True
    # A - rec なのは交互にmax,minが変わるから
    dp[i][j] = max(A[i] - rec(i+1, j), A[j] - rec(i, j-1))
    return dp[i][j]

print(rec(0, N-1))