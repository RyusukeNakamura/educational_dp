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

dp = [[[-1 for k in range(N+1)] for j in range(N+1)] for i in range(N+1)]

def rec(i, j, k):
    if dp[i][j][k] >= 0:
        return dp[i][j][k]
    if i==0 and j==0 and k==0:
        return 0.0
    
    res = 0.0
    if i > 0:
        res += rec(i-1, j, k) * i
    if j > 0:
        res += rec(i+1, j-1, k) * j
    if k > 0:
        res += rec(i, j+1, k-1) * k
    res += N
    res /= (i + j + k)

    dp[i][j][k] = res
    return res

print(rec(one, two, three))