n = int(input())
abc = tuple(tuple(map(int, input().split())) for _ in range(n))

dp = [[0 for j in range(3)] for _ in range(n+1)]

for i in range(n):
    for k in range(3):
        dp[i+1][k] = max(dp[i][j] + abc[i][k] for j in range(3) if j != k)
    
print(max(dp[-1]))