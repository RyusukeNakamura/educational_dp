import sys
sys.setrecursionlimit(10**5)
N = int(input())
adj = [[] for _ in range(N)]
for i in range(N-1):
    x, y = map(int, input().split())
    adj[x-1].append(y-1)
    adj[y-1].append(x-1)

mod = 10**9 + 7

def rec(i, p):
    w = 1
    b = 1
    for j in adj[i]:
        if j == p:
            continue
        rw, rb = rec(j, i)
        w *= (rw + rb) % mod
        b *= rw % mod
    return w, b

print(sum(rec(0, -1))% mod)