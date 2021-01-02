import sys
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
dp = [-1 for i in range(N+1)]
G = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    G[x-1].append(y-1)


def rec(v):
    # 既に探索されたところは再利用
    if dp[v] != -1:
        return dp[v]
    
    l = 0
    for nv in G[v]:
        l = max(l, rec(nv)+1)
    dp[v] = l
    return l

ans = 0
for i in range(N):
    ans = max(ans, rec(i))
print(ans)